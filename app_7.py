def main():
    st.write('# Telemarketing Analysis')
    st.markdown("---")
    
    # Apresenta a imagem na barra lateral
    image = Image.open("Bank-Branding.jpg")
    st.sidebar.image(image)

    # Botão para carregar arquivo na aplicação
    st.sidebar.write("## Suba o arquivo")
    data_file_1 = st.sidebar.file_uploader("Bank marketing data", type=['csv','xlsx'])

    # Verifica se há conteúdo carregado na aplicação
    if data_file_1 is not None:
        bank_raw = load_data(data_file_1)
        bank = bank_raw.copy()

        st.write('## Antes dos filtros')
        st.write(bank_raw.head())

        with st.sidebar.form(key='my_form'):

            # SELECIONA O TIPO DE GRÁFICO
            graph_type = st.radio('Tipo de gráfico:', ('Barras', 'Pizza'))
        
            # IDADES
            max_age = int(bank.age.max())
            min_age = int(bank.age.min())
            idades = st.slider(label='Idade', 
                               min_value=min_age,
                               max_value=max_age, 
                               value=(min_age, max_age),
                               step=1)
            
            # Botão de envio
            submit_button = st.form_submit_button(label='Aplicar')

        # Processa as seleções apenas se o botão de envio for pressionado
        if submit_button:
            st.write(f"Gráfico selecionado: {graph_type}")
            st.write(f"Idades selecionadas: {idades}")

# Inicia a aplicação
if __name__ == '__main__':
    main()



