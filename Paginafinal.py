# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta o abrimos el folder desde visual Studio Code 

# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Opcional: Activaremos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# deactivate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit
# pip install streamlit_option_menu
# pip install streamlit.components.v1

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu ordenador.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu ordenador.
# OJO: Debes antes tener instalado Streamlit en tu ordenador, 
## también debes antes definir la ruta de tus archivos y 
## tener un script de Python (nombre_de_tu_script.py) que quieras ejecutar en Streamlit.
# python -m streamlit run Paginafinal.py
# python -m streamlit run nombre_de_tu_script.py

# Librería principal para desarrollar aplicaciones web con Streamlit.
import streamlit as st
# Herramienta para crear menús de navegación personalizados en Streamlit.
from streamlit_option_menu import option_menu
# Este módulo permite incrustar componentes personalizados escritos en HTML, CSS y JavaScript dentro de una aplicación.
# components.html() permite mostrar código HTML interactivo directamente en la interfaz.
import streamlit.components.v1 as components

# Menú vertical en una barra lateral
# Crea una barra lateral (sidebar) en la aplicación.
with st.sidebar:
    opciones = option_menu(None,['Inicio', 'Corea del Sur', 'Japón', 'Tailandia'] , 
        icons=['airplane','hearts', 'flower3', 'sun-fill'], menu_icon="filetype-py", default_index=0)
    # Crea un menú de opciones dentro de la barra lateral -> option_menu(...)
    # Título que se mostrará encima del menú -> "Selecciona una sección: "
    # Lista de opciones disponibles para navegar -> ['Inicio', 'Corea', 'Japón', 'Tailandia']
    # Iconos asociados a cada opción del menú -> ['0-circle','1-circle', '2-circle']
    # Icono principal que aparece junto al título del menú -> menu_icon="filetype-py"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0

# Menú horizontal en una barra horizontal
# OJO: Se puede eliminar el título del menú con None
# Crea un menú de navegación horizontal y guarda la opción seleccionada por el usuario en la variable 'selected'
# selected = option_menu(
    # menu_title="Selecciona una sección: ", 
    # options=['Inicio', 'Experiencia', 'Gráficos'], 
    # icons=['person-heart', 'globe-americas', 'pencil-square'], 
    # menu_icon="cast", default_index=0, orientation="horizontal")
    # Título que aparece antes de las opciones del menú -> menu_title="Selecciona una sección: "
    # Lista de opciones que estarán disponibles en el menú -> ['Inicio', 'Experiencia', 'Gráficos']
    # Iconos asociados a cada opción del menú -> ['person-heart', 'globe-americas', 'pencil-square']
    # Icono principal que aparece junto al título del menú -> menu_icon="cast"
    # Opción seleccionada por defecto (0 = Inicio) -> default_index=0
    # Hace que el menú se muestre horizontalmente en lugar de verticalmente -> orientation="horizontal"

# Verifica si el usuario ha seleccionado la opción "Inicio" en el menú de navegación horizontal.
# OJO: En caso que elijas el menú de la barra lateral (sidebar) debes cambiar "selected" por "opciones"
if opciones == 'Inicio':
    st.markdown("<h1 style='text-align: center; color: #B0A5FA;'>.ೃ࿔ ✈︎ *:･MODO ASIA･:* ✈︎ ࿔ೃ.</h1>", unsafe_allow_html=True)
    # Muestra un título principal utilizando HTML -> st.markdown("...", unsafe_allow_html=True)
    # La etiqueta <h1> define un encabezado de nivel 1 -> "<h1 ...>...</h1>"
    # El estilo CSS 'text-align: center' centra el texto -> style='text-align: center;'
    # unsafe_allow_html=True permite que Streamlit interprete y renderice el código HTML incluido en la cadena
    texto_bienvenida = """
    ¡Bienvenid@ a Modo Asia! 🌏✈️

    Prepárate para un viaje virtual a través de Corea, Japón y Tailandia.
    En esta página web podrás encontrar:
    
    🎧Descubrir artistas
    
    🎬Encontrar tu próxima serie o película favorita
    
    🏯Explorar lugares turísticos

    ¡Todo esto y mucho más te espera en Modo Asia! 
    
    """
    st.markdown(texto_bienvenida)
    st.markdown("-----------------------------")
    st.markdown("<h2 style='text-align: center; color: #8DD1F0;'>˖𓍢ִ໋🍃˚¡Explora los destinos!˖𓍢ִ໋🍃˚</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Descubre un adelanto de lo que cada país tiene para ti: </p>", unsafe_allow_html=True)
    # Crea dos columnas de igual tamaño para organizar el contenido de forma horizontal en la aplicación.
    col1, col2 = st.columns(2, vertical_alignment="center")

    # Muestra una imagen en la primera columna
    with col1:
        st.subheader("🇰🇷 Corea del Sur")
        st.image("krs.jpg", caption="Un lugar donde la tradición y la modernidad se encuentran.")

    with col2:
        texto= """
        Corea del Sur es un país que combina tradición y modernidad.
        Es el país que la está rompiendo en todo el mundo. 
        El balance perfecto entre templos antiguos y la tecnología futurista de Seúl. 
        Básicamente, es la casa de la "Ola Coreana" (Hallyu), el lugar que nos dio el fenómeno del K-Pop, los K-Dramas maratoneables y una comida increíble que se volvió súper viral en redes.
        ¡Un destino que sí o sí tienes que conocer!
        """
        st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)
   
    col1, col2 = st.columns(2, vertical_alignment="center")
    with col1:
        st.subheader("🇯🇵 Japón")
        st.image("jpn1.webp", caption="Donde el anime, la tecnología y la historia se cruzan.")
    with col2:
        texto= """
        El paraíso de la cultura pop, el anime y los videojuegos. 
        Japón es otro nivel: puedes pasar de la paz de los templos antiguos en Kioto al caos lleno de luces neón y tiendas geek de Shibuya o Akihabara en Tokio. 
        Además, su comida es de las mejores del planeta (¡mucho más allá del sushi!) y es un lugar único donde el pasado tradicional y el futuro tecnológico chocan en cada esquina.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)
   
    col1, col2 = st.columns(2, vertical_alignment="center")
    with col1:
        st.subheader("🇹🇭 Tailandia")
        st.image("tln1.jpeg", caption="Un país de esencia tropical, templos majestuosos y buena vibra.")
    with col2:
        texto= """
        Una buena vibra, playas paradisíacas que parecen sacadas de un fondo de pantalla e historias súper atrapantes.
        Tailandia es mundialmente famosa por sus templos dorados gigantes, sus locos mercados flotantes y una comida callejera  extraordinaria.
        Además, su industria del entretenimiento está creciendo muchísimo con series románticas y de misterio que se están volviendo ultra virales en TikTok y Netflix.
        """
        st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #8DE0A4;'>Si te interesó alguno de los destinos, por favor, presiona el botón lateral correspondiente y descubre nuevos mundos! 📍🗺️ </h2>", unsafe_allow_html=True)
    

    
elif opciones == 'Corea del Sur':
    st.markdown("<h2 style='text-align: center;color:#AFFAB9'>Conoce más de Corea del Sur!🍙</h2>", unsafe_allow_html=True)
    # Agregamoa un texto introductorio sobre Corea del Sur
    texto = """
    ¡Qué gran decisión explorar a fondo la tierra del K-Pop! 🎶
    <br><br>
    Si el inicio te dio curiosidad, agárrate, porque aquí nos ponemos en modo fan
    <br><br>
    Descubre el lado más viral de Corea del Sur: grupos de K-Pop, series y películas que están rompiendo récords de audiencia, y los lugares más increíbles que te harán sentir dentro de un K-Drama.
    <br><br>
    👇 Abre el menú de abajo y escoje lo que más te llame la atención
    """
    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto}</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    categorias = ['Música', 'Series/Pelis', 'Lugares turísticos']
    categorias_seleccionadas = st.selectbox('Escoje un mundo distinto:', categorias)
    if categorias_seleccionadas == 'Música':
        st.subheader("💿 Música coreana")
        artistas_text = """
        🌟 Top 5 Artistas Coreanos que tienes que escuchar:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{artistas_text}</div>", unsafe_allow_html=True)

    # Primer grupo, NCT
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("1. NCT")
            st.image("nct.webp", caption="NCT revolucionó el K-Pop con su concepto de subunidades y sonido experimental.", use_container_width=True)
        with col2:
            texto_nct = """
            <b>ARTISTA:</b> Grupo multicultural / Proyecto global de K-Pop.
            <br><br>
            <b>GÉNERO:</b> K-Pop experimental, Hip-hop, Neo-soul y R&B.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Súper futurista, vanguardista y neo-cyberpunk. Destacan por usar ropa de diseñador de estilo utilitario, piezas asimétricas, colores neón, escenografías llenas de glitches tecnológicos y un concepto visual muy 'Neo' que rompe las reglas tradicionales.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_nct}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("2. SEVENTEEN")
            st.image("seventeen.jpg", caption="Seventeen es mundialmente famoso por producir sus propias canciones y coreografías perfectas.", use_container_width=True)
        with col2:
            texto_svt = """
            <b>ARTISTA:</b> Grupo de K-Pop (Boyband masiva de 13 integrantes).
            <br><br>
            <b>GÉNERO:</b> K-Pop, Synth-pop, Funk, R&B comercial y Dance-pop.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Energía pura, frescura y elegancia grupal. Pasan de una vibra súper juvenil y colorida (estilo retro/colegial) a trajes de alta costura perfectamente coordinados. Sus videos destacan por la sincronización matemática de sus integrantes en escenarios gigantes y coloridos.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_svt}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("3. AESPA")
            st.image("aespa.webp", caption="aespa destaca por conectar la música pop con avatares virtuales en el metaverso.", use_container_width=True)
        with col2:
            texto_aespa = """
            <b>ARTISTA:</b> Grupo femenino de K-Pop (Girlband).
            <br><br>
            <b>GÉNERO:</b> K-Pop hiper-energético, Hyperpop, EDM y Hip-hop futurista.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Estética Cyberpunk, Y2K digital y alta fantasía de videojuegos. Sus visuales están repletos de Inteligencia Artificial, criaturas de cristal en CGI, colores metálicos, maquillaje holográfico y prendas de cuero ajustadas tipo guerreras espaciales. ¡Súper aesthetic!
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_aespa}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("4. BIBI")
            st.image("bibi.webp", caption="BIBI ha roto el internet varias veces con su estilo rebelde y sin filtros.", use_container_width=True)
        with col2:
            texto_bibi = """
            <b>ARTISTA:</b> Cantante, rapera y compositora solista.
            <br><br>
            <b>GÉNERO:</b> K-HipHop, R&B alternativo y Dark-pop.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Atrevida, rebelde y estilo 'bad girl' del cine coreano. Su sello son los dos puntos rojos maquillados bajo sus ojos. Mezcla un estilo callejero muy urbano de Seúl con elementos góticos, outfits oscuros y una actitud cruda que la aleja por completo de la típica imagen 'perfecta'.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_bibi}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("5. THE ROSE")
            st.image("therose.jpg", caption="The Rose es el máximo referente del K-Rock indie en los festivales más grandes del mundo.", use_container_width=True)
        with col2:
            texto_therose = """
            <b>ARTISTA:</b> Banda de Rock / Indie Coreano (K-Rock).
            <br><br>
            <b>GÉNERO:</b> Indie rock, pop rock y rock alternativo emocional.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Nostálgica, poética y de estilo 'indie sleaze'. Predomina la iluminación tenue, los filtros de fotografía analógica, ropa oversize, chaquetas de cuero desgastadas y una atmósfera íntima cargada de melancolía que rompe la estética plástica del pop comercial.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_therose}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")
    elif categorias_seleccionadas == 'Series/Pelis':
        st.subheader("𓍢ִ໋⋆🎞️ Productos audiovisuales coreanos")
        artistas_text = """
        🌟 Top 5 series/ pelis coreanas que tienes que ver:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{artistas_text}</div>", unsafe_allow_html=True)

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Si la vida te da mandarinas (폭싹 속았수다)")
            st.image("mandarinas.jpg", caption="Un emotivo e inolvidable viaje a través de las estaciones de la vida y el amor.", use_container_width=True)
        with col2:
            texto_mandarinas = """
            <b>SINOPSIS:</b> Ambientada en la vibrante isla de Jeju, narra la historia de amor y superación de Ae-soon, una joven rebelde de los años 50 que sueña con ser poeta a pesar de la pobreza, y Gwan-sik, un joven silencioso y sumamente dedicado que la apoya incondicionalmente. La trama avanza a lo largo de las décadas y las estaciones del año, mostrando sus luchas generacionales y familiares.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Serie de televisión (2025) | 16 episodios.
            <br>
            • <b>Director:</b> Kim Won-suk.
            <br>
            • <b>Género:</b> Drama, Romance, Melodrama histórico.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_mandarinas}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        # ================= 2. PARASITE (INVERTIDO) =================
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            texto_parasite = """
            <b>SINOPSIS:</b> Tanto Gi-taek como su familia están sin trabajo. Cuando su hijo mayor, Gi-woo, empieza a dar clases particulares en la adinerada casa de los Park, ambas familias, que pertenecen a mundos completamente opuestos, comienzan a entrelazarse en una serie de eventos inesperados llenos de humor negro, mentiras y una fuerte crítica social.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Película (2019) | 132 minutos.
            <br>
            • <b>Director:</b> Bong Joon-ho.
            <br>
            • <b>Género:</b> Drama, Suspenso, Sátira social.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_parasite}</div>", unsafe_allow_html=True)
        with col2:
            st.subheader("Parasite (기생충)")
            st.image("parasite.jpg", caption="La histórica ganadora de 4 Premios Óscar, incluyendo Mejor Película.", use_container_width=True)
        st.markdown("-----------------------------")

        # ================= 3. SQUID GAME =================
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Squid Game (오징어 게임)")
            st.image("squidgame.jpg", caption="El fenómeno mundial que redefinió las series de supervivencia en streaming.", use_container_width=True)
        with col2:
            texto_squid = """
            <b>SINOPSIS:</b> Cientos de jugadores con graves problemas económicos aceptan una misteriosa invitación para competir en un juego infantil de supervivencia. Dentro les espera un tentador premio millonario, pero los desafíos son letales y ponen a prueba la moral, la desesperación y la naturaleza humana en su nivel más extremo.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Serie de televisión (2021) | 9 episodios.
            <br>
            • <b>Director:</b> Hwang Dong-hyuk.
            <br>
            • <b>Género:</b> Thriller, Suspenso, Drama de supervivencia.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_squid}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        # ================= 4. TRAIN TO BUSAN (INVERTIDO) =================
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            texto_busan = """
            <b>SINOPSIS:</b> Un brote viral misterioso pone a Corea del Sur en estado de emergencia. Un padre divorciado y su pequeña hija suben a un tren de alta velocidad que viaja de Seúl a Busán, pero justo antes de partir, una mujer infectada sube a bordo, transformando el trayecto en una claustrofóbica y desesperada lucha por sobrevivir.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Película (2016) | 118 minutos.
            <br>
            • <b>Director:</b> Yeon Sang-ho.
            <br>
            • <b>Género:</b> Acción, Terror, Suspenso (Zombies).
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_busan}</div>", unsafe_allow_html=True)
        with col2:
            st.subheader("Train to Busan (부산행)")
            st.image("busan.jpg", caption="Aclamada mundialmente como una de las mejores películas de zombies de la historia.", use_container_width=True)
        st.markdown("-----------------------------")

        # ================= 5. CRASH LANDING ON YOU =================
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Crash Landing on You (사랑의 불시착)")
            st.image("cloy.jpg", caption="Uno de los K-dramas románticos más exitosos y queridos de la televisión coreana.", use_container_width=True)
        with col2:
            texto_cloy = """
            <b>SINOPSIS:</b> Yoon Se-ri, una exitosa heredera y empresaria surcoreana, sufre un accidente de parapente debido a un tornado y termina realizando un aterrizaje de emergencia en Corea del Norte. Allí conoce a Ri Jeong-hyeok, un estricto oficial del ejército norcoreano que decide esconderla y protegerla, desencadenando un romance tan peligroso como inolvidable.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Serie de televisión (2019) | 16 episodios.
            <br>
            • <b>Director:</b> Lee Jung-hyo.
            <br>
            • <b>Género:</b> Romance, Drama, Comedia.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_cloy}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")
    elif categorias_seleccionadas == 'Lugares turísticos':
        st.subheader("⛩️ Lugares turísticos de Corea del Sur")
        lugares_text = """
        🌟 Top 5 Lugares turísticos de Corea del Sur que tienes que visitar:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{lugares_text}</div>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Seúl</h3>", unsafe_allow_html=True)
                st.image("seul.jpg", use_container_width=True)
                info_seoul = """
                <b>Ubicación:</b> Región Capital de Seúl.<br>
                <b>Clima:</b> Continental húmedo (mejor en primavera y otoño).<br>
                <b>Transporte:</b> Red del Metro de Seúl y trenes KTX.<br><br>
                <b>Actividades principales:</b><br>
                • Recorrer el Palacio Gyeongbokgung con vestimenta tradicional.<br>
                • Visitar el distrito tecnológico y de diseño Dongdaemun.<br>
                • Observar la vista panorámica desde la N Seoul Tower.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_seoul}</div>", unsafe_allow_html=True)

        with col2:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Isla Jeju</h3>", unsafe_allow_html=True)
                st.image("jeju.jpg", use_container_width=True)
                info_jeju = """
                <b>Ubicación:</b> Provincia Autónoma Especial de Jeju.<br>
                <b>Clima:</b> Subtropical templado (veranos cálidos e inviernos suaves).<br>
                <b>Transporte:</b> Vuelos internos directos o ferry desde Busan.<br><br>
                <b>Actividades principales:</b><br>
                • Subir al cráter volcánico Seongsan Ilchulbong al amanecer.<br>
                • Explorar los túneles de lava de Manjanggul.<br>
                • Visitar las cascadas de Cheonjiyeon y sus senderos naturales.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_jeju}</div>", unsafe_allow_html=True)

        with col3:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Busan</h3>", unsafe_allow_html=True)
                st.image("bubusan.webp", use_container_width=True)
                info_busan = """
                <b>Ubicación:</b> Costa sureste de Corea del Sur.<br>
                <b>Clima:</b> Subtropical húmedo (veranos costeros templados).<br>
                <b>Transporte:</b> Tren de alta velocidad KTX desde Seúl.<br><br>
                <b>Actividades principales:</b><br>
                • Caminar por las calles coloridas de Gamcheon Culture Village.<br>
                • Visitar el Templo Haedong Yonggungsa junto al mar.<br>
                • Recorrer la playa de Haeundae y el mercado Jagalchi.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_busan}</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Bukchon Hanok Village</h3>", unsafe_allow_html=True)
                st.image("bukchon.jpg", use_container_width=True)
                info_bukchon = """
                <b>Ubicación:</b> Jongno-gu, Seúl.<br>
                <b>Clima:</b> Continental (muy fotogénico con nieve o flores de cerezo).<br>
                <b>Transporte:</b> Línea 3 del metro de Seúl, estación Anguk.<br><br>
                <b>Actividades principales:</b><br>
                • Pasear entre cientos de casas tradicionales coreanas (hanoks).<br>
                • Visitar centros culturales, casas de té y talleres de artesanías.<br>
                • Tomar fotografías de la arquitectura de la dinastía Joseon.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_bukchon}</div>", unsafe_allow_html=True)

        with col2:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Isla de Nami</h3>", unsafe_allow_html=True)
                st.image("nami.avif", use_container_width=True)
                info_nami = """
                <b>Ubicación:</b> Chuncheon, provincia de Gangwon.<br>
                <b>Clima:</b> Templado (espectacular en otoño por las hojas rojas y doradas).<br>
                <b>Transporte:</b> Tren de cercanías ITX-Cheongchun hasta estación Gapyeong y luego ferry.<br><br>
                <b>Actividades principales:</b><br>
                • Caminar por los icónicos senderos flanqueados por altos árboles de metasecuoya.<br>
                • Recorrer la isla en bicicleta alquilada o caminando de forma relajada.<br>
                • Visitar los spots fotográficos famosos por salir en dramas románticos.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_nami}</div>", unsafe_allow_html=True)
        
    # Formato A
    # Agregamos todo los videos realizados en las prácticas anteriores
    # Muestra un subtítulo para identificar el contenido del video
    # st.subheader("🎥 Video 1 - YouTube")
    # Inserta un video de YouTube directamente en la aplicación.
    # El usuario puede reproducirlo sin salir de Streamlit.
    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")
    # Agrega una breve descripción del video.
    #st.caption(
    #    "En este video se presenta ...., "
    #)

    # Formato B
    # Muestra un subtítulo para identificar el contenido del video
    #st.subheader("🎥 Video 1 - Google Drive")
    # Crea un botón que redirige al usuario a un video alojado en Google Drive. 
    # Al hacer clic, el video se abrirá en una nueva pestaña del navegador.
    #st.link_button(
    #        "Ver video",
    #        "https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link"
    #    )
    # Agrega una breve descripción del video.
    #st.caption(
    #    "En este video se presenta ...., "
    #)

elif opciones == 'Japón':
    st.markdown("<h2 style='text-align: center; color:#FAAFE8'>Conoce más de Japón!🍡🌸</h2>", unsafe_allow_html=True)
    texto_3 = """
    ¡Qué gran decisión explorar a fondo la tierra del sol naciente! 🔆
    <br><br>
    Si el inicio te dio curiosidad, agárrate, porque aquí nos ponemos en modo geek
    <br><br>
    Descubre el lado más viral de Japón: openings inolvidables, artistas icónicos y los lugares más increíbles que te harán sentir dentro de un anime.
    <br><br>
    👇 Abre el menú de abajo y escoje lo que más te llame la atención
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_3}</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    categorias = ['Música', 'Series/Pelis', 'Lugares turísticos']
    categorias_seleccionadas = st.selectbox('Escoje un mundo distinto:', categorias)

    # Mostramos la categoría seleccionada
    if categorias_seleccionadas == 'Música':
        # Título de la sección
        st.subheader("(ᯤ) El ritmo de Japón")

        artistas_text = """
        🌟 Top 5 Artistas Japoneses que tienes que escuchar:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{artistas_text}</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("ONE OK ROCK")
            st.image("oneokrock.jpg", caption="ONE OK ROCK es una banda de rock japonesa formada en 2005.")

        with col2:
            texto= """
            <b>ARTISTA:</b> Banda de rock japonesa.
            <br><br>
            <b>GÉNERO:</b> Rock alternativo, pop rock, post-hardcore y arena rock.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Urbana, moderna y minimalista, con predominio de colores oscuros, prendas de cuero y denim, e inspiración en el rock contemporáneo.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Ado")
            st.image("ado.jpg", caption="Ado es una cantante solista japonesa conocida por su poderosa voz.")
        with col2:
            texto_ado = """
            <b>ARTISTA:</b> Solista.
            <br><br>
            <b>GÉNERO:</b> J-pop, rock, pop, vocaloid-inspired y anisong.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Misteriosa y oscura, con ilustraciones de estilo anime, colores intensos, contrastes marcados y una identidad visual que evita mostrar su rostro.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_ado}</div>", unsafe_allow_html=True)

        st.markdown("-----------------------------")
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Fujii Kaze")
            st.image("fujiikaze.jpg", caption="Fujii Kaze es un cantautor japonés que ha revolucionado la escena del pop.")
        with col2:
            texto_kaze = """
            <b>ARTISTA:</b> Solista.
            <br><br>
            <b>GÉNERO:</b> J-pop, R&B, soul, jazz y pop.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Natural, elegante y minimalista, con tonos neutros, moda casual y una imagen relajada que transmite autenticidad.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_kaze}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Vaundy")
            st.image("vaundy.jpg", caption="Vaundy es un artista multidisciplinar, cantante, compositor y productor.")
        with col2:
            texto_vaundy = """
            <b>ARTISTA:</b> Solista.
            <br><br>
            <b>GÉNERO:</b> J-pop, indie pop, rock alternativo, hip hop y electrónica.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Creativa y contemporánea, con inspiración retro, colores vibrantes, elementos artísticos y una imagen juvenil y experimental.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_vaundy}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Nujabes")
            st.image("nujabes.jpg", caption="Nujabes fue un influyente productor y DJ, pionero del lo-fi hip hop.")
        with col2:
            texto_nujabes ="""
            <b>ARTISTA:</b> Solista, productor musical y DJ.
            <br><br>
            <b>GÉNERO:</b> Hip hop instrumental, jazz rap, lo-fi hip hop y jazz.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Minimalista, nostálgica y urbana, con tonos suaves, paisajes cotidianos y una fuerte inspiración en el jazz y la cultura japonesa contemporánea.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_nujabes}</div>", unsafe_allow_html=True)
    
    elif categorias_seleccionadas == 'Series/Pelis':
        # Título de la sección
        st.subheader("🎥✮⋆˙Productos audiovisuales japoneses")
        artistas_text = """
        🌟 Top 5 series/ pelis japonesas que tienes que ver:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{artistas_text}</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Alice in Borderland")
            st.image("aib.jpg", caption="Una de las series de supervivencia más vistas a nivel mundial.", use_container_width=True)
        with col2:
            texto_alice = """
            <b>SINOPSIS:</b> Arisu, un joven perezoso y desempleado con una innegable pasión por los videojuegos, se encuentra de pronto con dos de sus amigos en una Tokio alternativa y desierta donde deberán superar sucesivas dificultades para sobrevivir.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            <br>
            • <b>Formato:</b> Serie (2020) | 22 Episodios.
            <br>
            • <b>Director:</b> Shinsuke Sato.
            <br>
            • <b>Género:</b> Ciencia ficción, Suspenso, Drama.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_alice}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            texto_monster = """
            <b>SINOPSIS:</b> Cuando su joven hijo Minato empieza a comportarse de forma extraña, su madre siente que algo va mal. Al descubrir que el responsable de todo ello es un profesor, irrumpe en la escuela exigiendo saber qué está pasando. Pero a medida que la historia se desarrolla a través de los ojos de los involucrados, la verdad sale a la luz...
            <br><br>
            <b>FICHA TÉCNICA:</b>
            <br>
            • <b>Formato:</b> Película (2023) | 126 min.
            <br>
            • <b>Director:</b> Hirokazu Koreeda.
            <br>
            • <b>Género:</b> Drama, Suspenso, Thriller psicológico.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_monster}</div>", unsafe_allow_html=True)
        with col2:
            st.subheader("Monster")
            st.image("monster.jpg", caption="Obra maestra ganadora a Mejor Guion en el Festival de Cannes.", use_container_width=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Perfect Days")
            st.image("pd.jpg", caption="Una hermosa reflexión sobre encontrar la felicidad en la rutina diaria.", use_container_width=True)
        with col2:
            texto_perfect = """
            <b>SINOPSIS:</b> Hirayama parece totalmente satisfecho con su sencilla vida de limpiador de retretes en Tokio. Fuera de su estructurada rutina diaria, disfruta de su pasión por la música y los libros. Le encantan los árboles y les hace fotos. Una serie de encuentros inesperados revelan poco a poco más de su pasado.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            <br>
            • <b>Formato:</b> Película (2023) | 119 min.
            <br>
            • <b>Director:</b> Wim Wenders.
            <br>
            • <b>Género:</b> Drama, Slice of life.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_perfect}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            texto_father = """
            <b>SINOPSIS:</b> Ryota, un exitoso arquitecto, lleva una vida tranquila junto a su familia. Todo cambia cuando descubre que el hijo que ha criado fue intercambiado por error en el hospital al nacer. Ambas familias deberán enfrentarse a una difícil decisión que cuestionará el verdadero significado de la paternidad y el amor.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            <br>
            • <b>Formato:</b> Película (2013) | 121 min.
            <br>
            • <b>Director:</b> Hirokazu Kore-eda.
            <br>
            • <b>Género:</b> Drama, Drama familiar.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_father}</div>", unsafe_allow_html=True)
        with col2:
            st.subheader("Like Father, Like Son")
            st.image("lfls.jpg", caption="Premio del Jurado en el Festival de Cannes.", use_container_width=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("All About Lily Chou-Chou")
            st.image("lcc.jpg", caption="Una película de culto que explora la crudeza de la juventud y el refugio de la música.", use_container_width=True)
        with col2:
            texto_lily = """
            <b>SINOPSIS:</b> En una pequeña ciudad japonesa, un grupo de adolescentes enfrenta el aislamiento, el acoso escolar y la violencia propia de la edad. Mientras sus vidas se entrelazan de formas dolorosas, encuentran refugio en la música de la enigmática cantante Lily Chou-Chou y en una comunidad virtual.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            <br>
            • <b>Formato:</b> Película (2001) | 146 min.
            <br>
            • <b>Director:</b> Shunji Iwai.
            <br>
            • <b>Género:</b> Drama, Coming-of-age, Psicológico.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_lily}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

    
    elif categorias_seleccionadas == 'Lugares turísticos':
        st.subheader("🗾 Lugares turísticos de Japón")
        artistas_text = """
        🌟 Top 5 Lugares turísticos de Japón que tienes que visitar:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{artistas_text}</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0;'>Fushimi Inari Taisha</h3>", unsafe_allow_html=True)
                st.image("fushimi.avif", use_container_width=True)
                info_fushimi = """
                <b>Ubicación:</b> Distrito de Fushimi, Kioto, Japón.<br>
                <b>Clima:</b> Templado (ideal en primavera y otoño).<br>
                <b>Transporte:</b> Tren JR hasta la estación Inari (línea JR Nara).<br><br>
                <b>Actividades principales:</b><br>
                • Recorrer los miles de torii rojos.<br>
                • Subir hasta la cima del monte Inari.<br>
                • Probar gastronomía típica en los puestos cercanos.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 14px; color: #555;'>{info_fushimi}</div>", unsafe_allow_html=True)

        with col2:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0;'>Monte Fuji</h3>", unsafe_allow_html=True)
                st.image("fuji.jpg", use_container_width=True)
                info_fuji = """
                <b>Ubicación:</b> Prefecturas de Shizuoka y Yamanashi.<br>
                <b>Clima:</b> Frío en la cumbre (ascenso de julio a agosto).<br>
                <b>Transporte:</b> Tren y autobús desde Tokio hasta estación Kawaguchiko.<br><br>
                <b>Actividades principales:</b><br>
                • Escalar la montaña en temporada oficial.<br>
                • Observar el amanecer desde la cumbre.<br>
                • Visitar los lagos contiguos y disfrutar de aguas termales (onsen).
                """
                st.markdown(f"<div style='text-align: justify; font-size: 14px; color: #555;'>{info_fuji}</div>", unsafe_allow_html=True)

        with col3:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0;'>Shibuya Crossing</h3>", unsafe_allow_html=True)
                st.image("shibuya.jpg", use_container_width=True)
                info_shibuya = """
                <b>Ubicación:</b> Distrito de Shibuya, Tokio, Japón.<br>
                <b>Clima:</b> Templado húmedo (veranos cálidos e inviernos frescos).<br>
                <b>Transporte:</b> Acceso directo desde la estación de Shibuya.<br><br>
                <b>Actividades principales:</b><br>
                • Cruzar el famoso paso peatonal.<br>
                • Visitar miradores, centros comerciales y tiendas.<br>
                • Disfrutar de restaurantes y cafeterías de la zona.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 14px; color: #555;'>{info_shibuya}</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True) # Espacio estético entre filas

        col1, col2= st.columns(2)

        with col1:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0;'>Bosque de Arashiyama</h3>", unsafe_allow_html=True)
                st.image("bambu.jpg", use_container_width=True)
                info_bambu = """
                <b>Ubicación:</b> Distrito de Arashiyama, Kioto, Japón.<br>
                <b>Clima:</b> Templado (ideal en primavera y otoño).<br>
                <b>Transporte:</b> Tren línea JR Sagano o línea Hankyu.<br><br>
                <b>Actividades principales:</b><br>
                • Pasear entre los altos bambúes.<br>
                • Recorrer el puente Togetsukyō y templos cercanos.<br>
                • Alquilar bicicletas o pasear en rickshaw.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 14px; color: #555;'>{info_bambu}</div>", unsafe_allow_html=True)

        with col2:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0;'>Santuario de Itsukushima</h3>", unsafe_allow_html=True)
                st.image("itsukushima.jpg", use_container_width=True)
                info_itsukushima = """
                <b>Ubicación:</b> Isla de Miyajima, Hiroshima, Japón.<br>
                <b>Clima:</b> Templado con inviernos suaves y veranos cálidos.<br>
                <b>Transporte:</b> Tren hasta Miyajimaguchi y transbordo a ferry.<br><br>
                <b>Actividades principales:</b><br>
                • Contemplar el famoso torii flotante en el mar.<br>
                • Convivir con los ciervos silvestres que habitan la isla.<br>
                • Degustar las ostras locales y dulces típicos (momiji manju).
                """
                st.markdown(f"<div style='text-align: justify; font-size: 14px; color: #555;'>{info_itsukushima}</div>", unsafe_allow_html=True)

        # Cargar el mapa HTML generado previamente
        # with open("mapa.html", "r", encoding="utf-8") as f:
        #    html_content = f.read()

        # Mostrar el mapa interactivo
        # components.html(
        #    html_content,
        #    height=600
        #)

elif opciones == 'Tailandia':
    st.markdown("<h2 style='text-align: center; color:#AFE5FA'>Conoce más de Tailandia!🌴🏯</h2>", unsafe_allow_html=True)
    texto_4 = """
    ¡Qué gran decisión explorar a fondo la tierra del elefante blanco! 🐘
    <br><br>
    Si el inicio te dio curiosidad, agárrate, porque aquí nos ponemos en modo tropical
    <br><br>
    Descubre el lado más viral de Tailandia: series románticas y de misterio que se están volviendo ultra virales en TikTok y Netflix.
    <br><br>
    👇 Abre el menú de abajo y escoje lo que más te llame la atención
    """
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_4}</div>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    categorias = ['Música', 'Series/Pelis', 'Lugares turísticos']
    categorias_seleccionadas = st.selectbox('Escoje un mundo distinto:', categorias)
    # Mostramos la categoría seleccionada
    if categorias_seleccionadas == 'Música':
        st.subheader("🎵 Música tailandesa")
        artistas_text = """
        🌟 Top 5 Artistas Tailandeses que tienes que escuchar:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{artistas_text}</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("1. LYKN")
            st.image("lykn.jpg", caption="LYKN es una de las boybands de T-Pop más influyentes de la actualidad.")
        with col2:
            texto_lykn = """
            <b>ARTISTA:</b> Boyband tailandesa (T-Pop).
            <br><br>
            <b>GÉNERO:</b> Dance-pop, R&B contemporáneo, synth-pop y hip-hop.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Estilo streetwear de alta gama combinado con moda futurista y utilitaria. Mucho uso de arneses, chaquetas estructuradas, colores neón contrastados con negros, y un look muy pulido de "idols" modernos.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_lykn}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("2. DEXX")
            st.image("dexx.jpg", caption="DEXX lidera la nueva ola del rock pesado y metalcore tailandés.")
        with col2:
            texto_dexx = """
            <b>ARTISTA:</b> Banda de rock / metal alternativo tailandesa.
            <br><br>
            <b>GÉNERO:</b> Metalcore, rock alternativo, post-hardcore y nu-metal.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Estética cyberpunk y oscura. Predomina el uso de ropa negra, cuero, cadenas, elementos tácticos/militares, máscaras o maquillaje disruptivo, y una iluminación en sus shows basada en luces de neón rojas y azules sobre fondos industriales.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_dexx}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("3. KT KRATAE (Kratae R-Siam)")
            st.image("kt.jpg", caption="Kratae fusiona la esencia folclórica de Tailandia con el pop global.")
        with col2:
            texto_kratae = """
            <b>ARTISTA:</b> Cantante, bailarina y ex-boxeadora tailandesa.
            <br><br>
            <b>GÉNERO:</b> Luk Thung moderno (música folclórica tailandesa combinada con pop), dance-pop, hip-hop y reguetón.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Maximalista, glamorosa y empoderada. Fusión de elementos tradicionales tailandeses con outfits de alta densidad de brillo (glitter, pedrería), looks estilo "gladiadora" o guerrera, y una fuerte inspiración en la cultura pop occidental (estilo Beyoncé/J-Lo).
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_kratae}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("4. MILLI")
            st.image("milli.jpg", caption="MILLI, la rapera solista que llevó el hip-hop de Bangkok a los escenarios globales.")
        with col2:
            texto_milli = """
            <b>ARTISTA:</b> Rapera y cantante solista tailandesa.
            <br><br>
            <b>GÉNERO:</b> Hip-hop, trap, deconstructed club y pop experimental.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Estética Y2K (años 2000), rebelde, colorida y sumamente ecléctica. Uso de ropa holgada mixturada con tops llamativos, accesorios extravagantes, peinados con trenzas o colores de fantasía, y una vibra muy urbana y juvenil de Bangkok.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_milli}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("5. THREE MAN DOWN")
            st.image("twmd.jpg", caption="Three Man Down es un referente absoluto del pop-rock e indie melancólico actual.")
        with col2:
            texto_tmd = """
            <b>ARTISTA:</b> Banda de rock tailandesa.
            <br><br>
            <b>GÉNERO:</b> Pop rock, indie pop, rock alternativo y synth-rock.
            <br><br>
            <b>ESTÉTICA VISUAL:</b> Estética retro-moderna, nostálgica e indie sleaze. Predominan las prendas vintage, camisas oversize estampadas, chaquetas denim desgastadas y filtros visuales que emulan la fotografía analógica de los 90, con una actitud relajada pero melancólica.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_tmd}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")
    elif categorias_seleccionadas == 'Series/Pelis':
        st.subheader("⋆📼˚Imperdibles proyectos tailandeses")
        artistas_text = """
        🌟 Top 5 series/ pelis tailandesas que tienes que ver:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{artistas_text}</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Khemjira (เขมจิรา)")
            st.image("khem.jpg", caption="Una atrapante historia que mezcla el romance BL con el misticismo tailandés.", use_container_width=True)
        with col2:
            texto_khemjira = """
            <b>SINOPSIS:</b> Narra la historia de Kem, un joven que descubre que su familia está ligada a una antigua maldición. Junto a Pharan, emprende un viaje para desentrañar el misterio que rodea a sus antepasados, enfrentándose a rituales, fuerzas sobrenaturales y creencias tradicionales mientras desarrolla un fuerte vínculo emocional.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Serie de televisión (2025) | 12 episodios.
            <br>
            • <b>Director:</b> Cheewin Thanamin Wongskulphat.
            <br>
            • <b>Género:</b> Romance BL, Fantasía, Misterio y Drama sobrenatural.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_khemjira}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            texto_girl = """
            <b>SINOPSIS:</b> Nanno es una misteriosa estudiante que aparece en diferentes colegios de Tailandia. En cada escuela expone la corrupción, la hipocresía y los abusos cometidos por estudiantes y profesores, haciendo que cada uno enfrente las consecuencias de sus acciones de maneras retorcidas.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Serie de antología (2018) | 2 temporadas, 21 episodios.
            <br>
            • <b>Director:</b> Diversos directores (P. Khumwan, K. Triwimol, S. Mongkolsiri).
            <br>
            • <b>Género:</b> Thriller psicológico, Misterio, Terror y Drama.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_girl}</div>", unsafe_allow_html=True)
        with col2:
            st.subheader("Girl From Nowhere (เด็กใหม่)")
            st.image("nanno.jpg", caption="La icónica Nanno y su venganza psicológica que se volvió un fenómeno global.", use_container_width=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("Bad Genius (ฉลาดเกมส์โกง)")
            st.image("bgen.jpg", caption="Uno de los thrillers cinematográficos más exitosos y tensos del cine asiático.", use_container_width=True)
        with col2:
            texto_genius = """
            <b>SINOPSIS:</b> Lynn, una brillante estudiante de secundaria, crea un sofisticado sistema para ayudar a otros alumnos a aprobar exámenes a cambio de dinero. Lo que comienza como un pequeño favor termina convirtiéndose en una operación internacional de alto riesgo, donde la inteligencia, la presión y la ética se ponen a prueba.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Película (2017) | 130 minutos.
            <br>
            • <b>Director:</b> Nattawut Poonpiriya.
            <br>
            • <b>Género:</b> Suspenso, Crimen y Drama.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_genius}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            texto_grandma = """
            <b>SINOPSIS:</b> M, un joven sin un rumbo claro en la vida, decide cuidar de su abuela gravemente enferma con la esperanza de heredar su fortuna. Sin embargo, mientras convive con ella, la codicia inicial se transforma al descubrir el verdadero significado de la familia, el amor y el sacrificio.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Película (2024) | 125 minutos.
            <br>
            • <b>Director:</b> Pat Boonnitipat.
            <br>
            • <b>Género:</b> Drama, Comedia y Familiar.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_grandma}</div>", unsafe_allow_html=True)
        with col2:
            st.subheader("How to Make Millions Before Grandma Dies")
            st.image("grandma.jpg", caption="La película que rompió récords de taquilla y corazones en todo el sudeste asiático.", use_container_width=True)
        st.markdown("-----------------------------")

        col1, col2 = st.columns(2, vertical_alignment="center")
        with col1:
            st.subheader("The Believers")
            st.image("thebel.webp", caption="Un drama moderno y provocador sobre el dinero y la fe.", use_container_width=True)
        with col2:
            texto_believers = """
            <b>SINOPSIS:</b> Tres jóvenes emprendedores, agobiados por las deudas, descubren una oportunidad de negocio inesperada y clandestina: transformar un templo budista descuidado en un negocio altamente rentable gracias al marketing. Mientras buscan el éxito masivo, enfrentarán dilemas éticos, religiosos y peligros personales.
            <br><br>
            <b>FICHA TÉCNICA:</b>
            • <b>Formato:</b> Serie (2024) | 9 episodios.
            <br>
            • <b>Director:</b> Wattanapong Wongwan.
            <br>
            • <b>Género:</b> Drama, Crimen y Suspenso.
            """
            st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_believers}</div>", unsafe_allow_html=True)
        st.markdown("-----------------------------")
    elif categorias_seleccionadas == 'Lugares turísticos':
        st.subheader("🗺️ Lugares turísticos de Tailandia")
        artistas_text = """
        🌟 Top 5 Lugares turísticos de Tailandia que tienes que visitar:
        """
        st.markdown(f"<div style='text-align: justify; font-size: 20px;'>{artistas_text}</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Gran Palacio de Bangkok</h3>", unsafe_allow_html=True)
                st.image("bangkok.jpg", use_container_width=True)
                info_palacio = """
                <b>Ubicación:</b> Centro histórico de Bangkok.<br>
                <b>Clima:</b> Tropical cálido y húmedo (25-35 °C).<br>
                <b>Transporte:</b> BTS Skytrain (estación Saphan Taksin + barco) o taxi.<br><br>
                <b>Actividades principales:</b><br>
                • Recorrer el palacio y el Templo del Buda Esmeralda.<br>
                • Admirar la arquitectura real e histórica.<br>
                • Conocer la historia de la monarquía tailandesa.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_palacio}</div>", unsafe_allow_html=True)

        with col2:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Wat Arun</h3>", unsafe_allow_html=True)
                st.image("wat.jpg", use_container_width=True)
                info_arun = """
                <b>Ubicación:</b> Orilla oeste del río Chao Phraya, Bangkok.<br>
                <b>Clima:</b> Tropical cálido y húmedo (25-35 °C).<br>
                <b>Transporte:</b> Barco por el río Chao Phraya, taxi o tuk-tuk.<br><br>
                <b>Actividades principales:</b><br>
                • Subir a la torre principal para ver los detalles.<br>
                • Contemplar el atardecer junto al río.<br>
                • Recorrer el templo y realizar fotografía de paisaje.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_arun}</div>", unsafe_allow_html=True)

        with col3:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Islas Phi Phi</h3>", unsafe_allow_html=True)
                st.image("phi.jpg", use_container_width=True)
                info_phiphi = """
                <b>Ubicación:</b> Mar de Andamán, entre Phuket y Krabi.<br>
                <b>Clima:</b> Tropical (seco de noviembre a abril).<br>
                <b>Transporte:</b> Ferry o lancha rápida desde Phuket o Krabi.<br><br>
                <b>Actividades principales:</b><br>
                • Practicar snorkel, buceo y kayak en aguas cristalinas.<br>
                • Realizar paseos en bote tradicional por las bahías.<br>
                • Hacer senderismo hacia los miradores o relajarse en la playa.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_phiphi}</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Parque Ayutthaya</h3>", unsafe_allow_html=True)
                st.image("ayu.jpg", use_container_width=True)
                info_ayutthaya = """
                <b>Ubicación:</b> Ciudad de Ayutthaya, a 80 km de Bangkok.<br>
                <b>Clima:</b> Tropical cálido y húmedo (24-35 °C).<br>
                <b>Transporte:</b> Tren, autobús, miniván o automóvil.<br><br>
                <b>Actividades principales:</b><br>
                • Recorrer las ruinas históricas de los antiguos templos.<br>
                • Pasear en bicicleta por el complejo arqueológico.<br>
                • Visitar los museos locales y realizar rutas guiadas.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_ayutthaya}</div>", unsafe_allow_html=True)

        with col2:
            with st.container(border=True):
                st.markdown("<h3 style='text-align: center; margin-top:0; font-size: 18px;'>Wat Doi Suthep</h3>", unsafe_allow_html=True)
                st.image("doi.jpg", use_container_width=True)
                info_suthep = """
                <b>Ubicación:</b> Monte Doi Suthep, cerca de Chiang Mai.<br>
                <b>Clima:</b> De montaña (más fresco de noviembre a febrero).<br>
                <b>Transporte:</b> Songthaew (camioneta compartida) o taxi.<br><br>
                <b>Actividades principales:</b><br>
                • Visitar el templo sagrado y subir la gran escalinata naga.<br>
                • Disfrutar de las vistas panorámicas hacia Chiang Mai.<br>
                • Participar u observar ceremonias budistas tradicionales.
                """
                st.markdown(f"<div style='text-align: justify; font-size: 13px; color: #555;'>{info_suthep}</div>", unsafe_allow_html=True)