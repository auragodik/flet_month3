import flet as ft
from datetime import datetime as datetime
def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.DARK

    greeting_text = ft.Text('hello world!')
    greeting_history = []
    history_text = ft.Text('История приветсвия: ')
    # def update_history():
    #     history_controls = [ft.Text('История приветствий: ')]
    
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

            greeting_history.append(f'{name}')
            history_text.value = 'История приветствий:\n ' + '\n'.join(greeting_history)
            

            
        else:    
            print('ничего не введено')
            greeting_text.value = 'пж введите имя или возраст'



        
        

        page.update()

        def theme_f(_):
            if ft.ThemeMode.LIGHT:
                name_i = ft.ThemeMode.DARK
                print(name_i)
            else:
                ft.ThemeMode.DARK
                name_d = ft.ThemeMode.LIGHT
                print(name_d)
            theme_f()
    
    name_input = ft.TextField(label='введите имя: ', on_submit=on_button_click)
    name_button = ft.ElevatedButton('send', on_click=on_button_click)
    def clear_history(_):
        greeting_history.clear()
        history_text.value = 'История приветствий'
        page.update()

    def dl_history(_):
        if greeting_history:
            greeting_history.pop()
            history_text.value = 'История приветствий:\n ' + '\n'.join(greeting_history)
        else:
            print('История пуста!')
            page.update()



    dl_button = ft.ElevatedButton('delete', on_click=dl_history)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)




    # page.add(greeting_text, name_input, age_input, name_button, clear_button, history_text)
    page.add(greeting_text, name_input, age_input, dl_button, history_text,
             ft.Row([name_button, clear_button], alignment=ft.MainAxisAlignment.CENTER)
            )
    

ft.app(target=main, view=ft.WEB_BROWSER)    

