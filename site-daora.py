import streamlit as st

st.set_page_config(page_title="SimRigCheck - O que roda?", page_icon="🎮", layout="centered")

st.title("🎮 SimRigCheck")
st.subheader("Descubra quais simuladores rodam no seu PC")
st.write("Selecione as configurações abaixo:")

st.markdown(
    """
    <style>
    div.stButton > button[kind="primary"] {
        background-color: #FF6600 !important;
        color: white !important;
        border: none !important;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #E65C00 !important;
        color: white !important;
    }
    .resultado-laranja {
        background-color: #FFF2E6;
        color: #CC5200;
        padding: 15px;
        border-radius: 5px;
        border-left: 5px solid #FF6600;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    cpu_escolha = st.selectbox(
        "Geração do Processador (CPU)",
        options=[
            "1ª até 5ª Geração (Mediano)", 
            "6ª até 9ª Geração (Incrivel!)", 
            "10ª Geração até a Atual (Perfeito!)"
        ]
    )
    if "1ª até 5ª" in cpu_escolha:
        cpu_usuario = 1
    elif "6ª até 9ª" in cpu_escolha:
        cpu_usuario = 2
    else:
        cpu_usuario = 3

with col2:
    gpu_escolha = st.selectbox(
        "Placa de Vídeo (GPU)",
        options=[
            "Integrada / GTX 750 Ti (é, tá médio)", 
            "GTX 1660 / RX 580 / RTX 2060 (Tá bom!)", 
            "RTX 3060 / RX 6600 ou superior (Que GPUs alienigenas são essas?!)"
        ]
    )
    if "Integrada" in gpu_escolha:
        gpu_usuario = 1
    elif "GTX 1660" in gpu_escolha:
        gpu_usuario = 2
    else:
        gpu_usuario = 3

with col3:
    ram_escolha = st.selectbox(
        "Memória RAM",
        options=["4 GB ou menos(minimo do minimo)", "8 GB(médio)", "16 GB(Balanciado)", "32 GB(Tá otimo!)", "64 GB ou superior(Tu tem dinheiro ein >:D)"]
    )
    
    ram_usuario = int(ram_escolha.split()[0])

jogos = [
    {
        "nome": "Assetto Corsa",
        "cpu_min": 1,  
        "gpu_min": 1,
        "ram_min": 8,
        "genero": "Simulador de entrada"
    },
    {
        "nome": "Assetto Corsa Competizione",
        "cpu_min": 2,  
        "gpu_min": 2,
        "ram_min": 16,
        "genero": "Simulador de Turismo"
    },    
    {
        "nome": "Le Mans Ultimate",
        "cpu_min": 1,  
        "gpu_min": 2,
        "ram_min": 16,
        "genero": "Simulador de Endurance"
    },
    {
        "nome": "Iracing",
        "cpu_min": 1,  
        "gpu_min": 2,  
        "ram_min": 16,
        "genero": "O goat dos simuladores de corrida"
    },
    {
        "nome": "Automobilista 1",
        "cpu_min": 1,  
        "gpu_min": 1,  
        "ram_min": 8,
        "genero": "Simulador de corrida brasileiro mais top"
    },
    {
        "nome": "Automobilista 2",
        "cpu_min": 1,  
        "gpu_min": 2,  
        "ram_min": 16,
        "genero": "Simulador de corrida brasileiro que é bom, mas não é tão bom quanto o 1"
    },
    {
        "nome": "Rfactor 1",
        "cpu_min": 1,  
        "gpu_min": 1,  
        "ram_min": 4,
        "genero": "Simulador que roda em qualquer coisa"
    },
    {
        "nome": "Rfactor 2",
        "cpu_min": 1,  
        "gpu_min": 2,  
        "ram_min": 16,
        "genero": "Simulador bom, mas que não roda em qualquer coisa"
    }
]

if st.button("Verificar Simuladores Compatíveis", type="primary"):
    st.write("### 🚀 Simuladores que rodam no seu PC:")
    
    jogos_compativeis = []
    
    for jogo in jogos:
        if (cpu_usuario >= jogo["cpu_min"] and 
            gpu_usuario >= jogo["gpu_min"] and 
            ram_usuario >= jogo["ram_min"]):
            
            jogos_compativeis.append(jogo)
            
    if jogos_compativeis:
        for jogo in jogos_compativeis:
            st.markdown(
                f'<div class="resultado-laranja"><b>{jogo["nome"]}</b> — <i>{jogo["genero"]}</i></div>', 
                unsafe_allow_html=True
            )
    else:
        st.error("Nenhum simulador do catálogo roda nessa configuração. Hora de jogar essa coisa que você chama de PC e dar um upgrade! 💻")
