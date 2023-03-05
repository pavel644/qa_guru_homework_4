def print_function_name_with_args(func, *args):
    func_name = func.__name__.replace('_', ' ').capitalize()
    print(f'{func_name} [{", ".join(args)}]')


def open_browser(browser_name):
    print_function_name_with_args(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_function_name_with_args(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_function_name_with_args(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name='Chrome')
go_to_companyname_homepage('https://qa.guru/')
find_registration_button_on_login_page('https://qa.guru/cms/system/login', 'Зарегистрироваться')
