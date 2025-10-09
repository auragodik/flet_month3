import flet as ft
from datetime import datetime as datetime
def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text('hello world!')
    name_input = ft.TextField(label='введите имя: ')
    age_input = ft.TextField(label='введите возраст')
    def on_button_click(_):
        name = name_input.value.strip()
        names = age_input.value.strip()
        now = datetime.now()
        formatted_time = f"{now.year:02}/{now.month:02}/{now.day:02} {now.hour:02}:{now.minute:02}:{now.second}"
        
        # print(name, names)
        if name:
            # print(greeting_text)
            greeting_text.value = f'{formatted_time}, Привет {name}, твой возраст {names} '
            print(greeting_text.value)
            name_input.value = ""
        else:    
            print('ничего не введено')
            greeting_text.value = 'пж введите имя или возраст'



        def theme_f(_):
            if ft.ThemeMode.LIGHT:
                name_i = ft.ThemeMode.DARK
                print(name_i)
            else:
                ft.ThemeMode.DARK
                name_d = ft.ThemeMode.LIGHT
                print(name_d)
            theme_f()
    
    name_button = ft.ElevatedButton('send', on_click=on_button_click)
    # name_button_text = ft.TextButton('send')
    # name_button_icon = ft.IconButton(icon=ft.Icons.SEND)
    theme_button = ft.IconButton(icon=ft.Icons.SWITCH_LEFT)
    




    page.add(greeting_text, name_input, name_button, theme_button, age_input)
ft.app(target=main, view=ft.WEB_BROWSER)    

