import os
import customtkinter
from PIL import Image

#~-- MIS IMPORTACIONES --~#
from funcion_abrir_webdrivers import abrir_webdrivers, cerrar_webdrivers
from funcion_venta import venta
#~-- MIS IMPORTACIONES --~#

def load_images(image_path):
# Prepara las imagenes que se van a utilizar
    images = {
        "logo_image": customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26)),
        "large_test_image": customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150)),
        "image_icon_image": customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20)),
        "home_image": customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                              dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20)),
        "chat_image": customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                              dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20)),
        "add_user_image": customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                  dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))
    }
    return images

def create_navigation_frame(root, images):
    navigation_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="black")
    navigation_frame.grid(row=0, column=0, sticky="nsew")
    navigation_frame.grid_rowconfigure(4, weight=1)
    navigation_frame_label = customtkinter.CTkLabel(navigation_frame, text="  Image Example", image=images["logo_image"],
                                                     compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
    navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
    home_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                           fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "#483D8B"),
                                           image=images["home_image"], anchor="w", command=lambda: select_frame("home"))
    home_button.grid(row=1, column=0, sticky="ew")
    frame_2_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                              fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "#483D8B"),
                                              image=images["chat_image"], anchor="w", command=lambda: select_frame("frame_2"))
    frame_2_button.grid(row=2, column=0, sticky="ew")
    frame_3_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                              fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "#483D8B"),
                                              image=images["add_user_image"], anchor="w", command=lambda: select_frame("frame_3"))
    frame_3_button.grid(row=3, column=0, sticky="ew")
    return home_button, frame_2_button, frame_3_button
"""
    appearance_mode_menu = customtkinter.CTkOptionMenu(navigation_frame, values=["Light", "Dark", "System"],
                                                        command=change_appearance_mode)
    appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")
    return home_button, frame_2_button, frame_3_button
"""


def create_home_frame(root, images):
    global home_frame_button_1, home_frame_button_2, home_frame_button_3, home_frame_button_4, home_frame_large_image_label
    home_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="gray5")
    #home_frame.grid(row=0, column=0)
    #home_frame.grid_columnconfigure(0, weight=1)
    home_frame_large_image_label = customtkinter.CTkLabel(home_frame, text="", image=images["large_test_image"])
    home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)
    home_frame_button_1 = customtkinter.CTkButton(home_frame,text="Abrir navegador", fg_color="#4169E1",hover_color="#483D8B",width=200, height=100,command=lambda:(pulsar_abrir_webdrivers(),abrir_webdrivers()))
    home_frame_button_1.grid(row=1, column=0)#, padx=20, pady=10,rowspan=2,sticky="nsew")
    home_frame_button_2 = customtkinter.CTkButton(home_frame, text="Cerrar \n navegador",fg_color="red",hover_color="#483D8B", corner_radius=0,width=20, height=20,command=lambda: ventana_cerrar_webdrivers(root))
    #home_frame_button_2.grid(row=2, column=0)#, padx=20, pady=40,rowspan=2,sticky="nsew")
    home_frame_button_3 = customtkinter.CTkButton(home_frame, text="Comprar", fg_color="#4169E1",hover_color="#483D8B",width=270, height=40)
    #home_frame_button_3.grid(row=1, column=1, padx=20, pady=10)
    home_frame_button_4 = customtkinter.CTkButton(home_frame, text="Vender", fg_color="#4169E1",hover_color="#483D8B",width=270, height=40,command=venta)
    #home_frame_button_4.grid(row=2, column=1, padx=20, pady=10)
    return home_frame

def create_frames(root):
    second_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")
    third_frame = customtkinter.CTkFrame(root, corner_radius=0, fg_color="transparent")
    return second_frame, third_frame

def select_frame(name):
    # Cambiar el color del botón para el botón seleccionado
    home_button.configure(fg_color="#4169E1" if name == "home" else "transparent")
    frame_2_button.configure(fg_color="#4169E1" if name == "frame_2" else "transparent")
    frame_3_button.configure(fg_color= "#4169E1" if name == "frame_3" else "transparent")

    # Mostrar el marco seleccionado
    if name == "home":
        home_frame.grid(row=0, column=1, sticky="nsew",padx=0,pady=0)
    else:
        home_frame.grid_forget()  
    if name == "frame_2":
        second_frame.grid(row=0, column=1, sticky="nsew",padx=0,pady=0)
    else:
        second_frame.grid_forget() 
    if name == "frame_3":
        third_frame.grid(row=0, column=1, sticky="nsew",padx=0,pady=0)
    else:
        third_frame.grid_forget()

def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

def main():
    global home_button, frame_2_button, frame_3_button, home_frame, second_frame, third_frame

    # Configuración inicial de la aplicación
    customtkinter.set_appearance_mode("Dark")  # Modo de apariencia inicial
    customtkinter.set_default_color_theme("blue")
    root = customtkinter.CTk()
    root.title("APP BOT")
    root.geometry("700x450")

    # Establecer el diseño de cuadrícula 1x2
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
    images = load_images(image_path)
    home_button, frame_2_button, frame_3_button = create_navigation_frame(root, images)
    home_frame = create_home_frame(root, images)
    second_frame, third_frame = create_frames(root)

    # Seleccionar el marco predeterminado
    select_frame("home")

    root.mainloop()
    return root

# Funciones añadidas
def ventana_cerrar_webdrivers(root):
    vcw = customtkinter.CTkToplevel(root)
    vcw.title("Cerrar navegador")
    x = root.winfo_x()  # Coordenada x de la ventana principal
    y = root.winfo_y()  # Coordenada y de la ventana principal
    w=root.winfo_width()//3
    h=root.winfo_height()//3
    x=x+w
    y=y+h

    # Establecer la posición de la ventana Toplevel para que se superponga
    vcw.geometry(f"400x100+{x}+{y}")
    vcw.attributes("-topmost", True)
    vcw.resizable(False, False)
    etiqueta1_vcw=customtkinter.CTkLabel(vcw,text="¿Quiere cerrar el navegador?")
    etiqueta1_vcw.place(relx=0.5, rely=0.2, anchor='center')
    boton_si_vcw=customtkinter.CTkButton(vcw,text="SÍ", command=lambda: (vcw.destroy(), cerrar_webdrivers(), pulsar_cerrar_webdrivers()))
    boton_si_vcw.place(relx=0.3, rely=0.6, anchor='center')
    boton_no_vcw=customtkinter.CTkButton(vcw,text="NO")
    boton_no_vcw.place(relx=0.7, rely=0.6, anchor='center')

def pulsar_abrir_webdrivers():
    home_frame_button_1.grid_forget()
    home_frame_button_2.place(relx=0.85, rely=0.85, anchor='center')#, padx=20, pady=40,rowspan=2,sticky="nsew")
    home_frame_button_3.grid(row=1, column=0, padx=10, pady=10)
    home_frame_button_4.grid(row=2, column=0, padx=10, pady=10)
    #añadir "funcion_abrir_webdrivers()"

def pulsar_cerrar_webdrivers():
    home_frame_button_1.grid(row=1, column=0)
    home_frame_button_2.place_forget()
    home_frame_button_3.grid_forget()
    home_frame_button_4.grid_forget()
    #añadir una funcion para detener los webdrivers sin conflictos

if __name__ == "__main__":
    main()