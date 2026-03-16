import streamlit as st
import pandas as pd
from api_client import ApiClient

st.set_page_config(page_title="Tirindicator - Indicação de Pneus", layout="wide")

# Interface Estilizada
st.markdown("""
<style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛞 Tirindicator")
st.subheader("O pneu ideal para o seu veículo")

menu = ["🏠 Home", "👤 Clientes", "🚗 Meus Veículos", "📊 Relatórios"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "🏠 Home":
    st.write("### Bem-vindo ao Tirindicator!")
    st.write("Cadastre seu veículo e descubra qual o melhor pneu para você baseado em dados técnicos.")
    st.image("https://images.unsplash.com/photo-1549443602-0e42d7119e09?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", caption="Manutenção Preventiva")

elif choice == "👤 Clientes":
    st.header("Gerenciamento de Clientes")
    
    with st.expander("Cadastrar Novo Cliente"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        if st.button("Salvar Cliente"):
            res = ApiClient.create_cliente(nome, email)
            if "id" in res:
                st.success(f"Cliente {nome} cadastrado com sucesso!")
            else:
                st.error(f"Erro ao cadastrar: {res.get('detail')}")

    st.write("---")
    st.subheader("Lista de Clientes")
    clientes = ApiClient.get_clientes()
    if isinstance(clientes, list) and clientes:
        df = pd.DataFrame(clientes)
        st.dataframe(df[["id", "nome", "email", "is_active"]], width="stretch")
    elif isinstance(clientes, dict) and "detail" in clientes:
        st.error(f"Erro na API: {clientes['detail']}")
    else:
        st.info("Nenhum cliente cadastrado ou erro na comunicação.")

elif choice == "🚗 Meus Veículos":
    st.header("Gerenciamento de Veículos")
    
    clientes = ApiClient.get_clientes()
    if not clientes:
        st.warning("Cadastre um cliente primeiro!")
    else:
        cliente_nomes = {c["nome"]: c["id"] for c in clientes}
        selected_cliente_nome = st.selectbox("Selecione o Cliente", list(cliente_nomes.keys()))
        cliente_id = cliente_nomes[selected_cliente_nome]

        with st.expander("Adicionar Veículo"):
            col1, col2 = st.columns(2)
            
            marcas = ApiClient.get_marcas()
            marca_options = {m["nome"]: m["codigo"] for m in marcas}
            selected_marca = col1.selectbox("Marca", list(marca_options.keys()))
            
            if selected_marca:
                modelos = ApiClient.get_modelos(marca_options[selected_marca])
                modelo_options = {mod["nome"]: mod["codigo"] for mod in modelos}
                selected_modelo = col1.selectbox("Modelo", list(modelo_options.keys()))
                
                if selected_modelo:
                    anos = ApiClient.get_anos(marca_options[selected_marca], modelo_options[selected_modelo])
                    ano_options = {a["nome"]: a["codigo"] for a in anos}
                    selected_ano_name = col2.selectbox("Ano/Versão", list(ano_options.keys()))
                    
                    motorizacao = col2.text_input("Motorização (ex: 1.6 Flex)")
                    categoria = col2.selectbox("Categoria", ["Sedan", "SUV", "Hatch", "Pick-up", "Crossover"])
                    
                    if st.button("Cadastrar Veículo"):
                        res = ApiClient.create_veiculo(
                            cliente_id, 
                            selected_marca, 
                            selected_modelo, 
                            selected_ano_name.split(" ")[0], 
                            motorizacao, 
                            categoria
                        )
                        st.success("Veículo cadastrado!")

        st.write("---")
        st.subheader("Veículos Cadastrados")
        veiculos = ApiClient.get_veiculos(cliente_id)
        if veiculos:
            for v in veiculos:
                with st.container():
                    col_v1, col_v2 = st.columns([3, 1])
                    col_v1.markdown(f"**{v['marca']} {v['modelo']}** ({v['ano']}) - {v['categoria']}")
                    if col_v2.button("💡 Ver Pneus", key=f"btn_{v['id']}"):
                        rec = ApiClient.get_recomendacao(v['id'])
                        st.write("#### Recomendações para você:")
                        for p in rec:
                            st.info(f"🛞 {p['marca']} {p['modelo']} | Medida: {p['largura']}/{p['perfil']} {p['aro']} | Preço Médio: R$ {p['preco_estimado']}")
        else:
            st.info("Este cliente ainda não possui veículos cadastrados.")

elif choice == "📊 Relatórios":
    st.header("Painel de Gestão")
    clientes = ApiClient.get_clientes()
    
    st.metric("Total de Clientes", len(clientes))
    
    # Aqui poderiam entrar gráficos do Plotly/Altair
    st.write("Dados consolidados em tempo real.")
