from selenium.webdriver.common.by import By


class MainPageLocators:
    """Locators for main page"""
    MAIN_PAGE_TITLE = "My Store"
    LOCATOR_SHOP_SEARCH_MAIN = (By.CSS_SELECTOR, "#header_logo > a > img")  # локатор главной страницы
    LOCATOR_SHOP_SEARCH_FIELD = (By.ID, "search_query_top")  # локатор поисковой строки
    LOCATOR_SHOP_SEARCH_BUTTON = (By.NAME, "submit_search")  # локатор кнопки “Найти”
    LOCATOR_SHOP_NAVIGATION_BAR = (By.CLASS_NAME, "columns-container")  # локатор навигации страницы
    LOCATOR_SHOP_SIGN_IN_LINK = (By.CLASS_NAME, "login")  # локатор для перехода на страницу логина
    LOCATOR_SHOP_CART_LINK = (By.CLASS_NAME, "shopping_cart")  # локатор для перехода на страницу корзины
    LOCATOR_SHOP_NAVIGATION_TAB_1 = (By.CLASS_NAME, "sf-with-ul")  # локатор для вкладки "Woman"
    LOCATOR_SHOP_NAVIGATION_TAB_2 = (
        By.CSS_SELECTOR, "#block_top_menu > ul > li:nth-child(2)")  # локатор для вкладки "Dresses"
    LOCATOR_SHOP_NAVIGATION_TAB_3 = (
        By.CSS_SELECTOR, "#block_top_menu > ul > li:nth-child(3)")  # локатор для вкладки "T-SHIRT"
    LOCATOR_SHOP_NAVIGATION_TAB_4 = (By.XPATH, "//*[@id='home-page-tabs']/li[1]/a")  # локатор для вкладки
    # "POPULAR"
    LOCATOR_SHOP_NAVIGATION_TAB_5 = (By.CSS_SELECTOR, "#home-page-tabs > li:nth-child(2) > a")  # локатор для вкладки
    # "BEST SELLERS"


class LoginPageLocators:
    """Locators for login"""
    LOCATOR_SIGN_IN = (By.CLASS_NAME, "login") # кнопка "Sign in"
    LOCATOR_SHOP_REGISTERED_LOGIN = (By.ID, "email")  # локатор окна ввода логина уже зарагестрированного пользователя
    LOCATOR_SHOP_REGISTERED_PASSWORD = (By.ID, "passwd")  # локатор окна ввода пароля
    LOCATOR_SHOP_SUBMIT_BUTTON = (By.ID, "SubmitLogin")  # локатор кнопки "Войти"
    LOGIN_PAGE_TITLE = "Login - My Store"
    LOCATOR_SHOP_LOGIN_PAGE = (By.CLASS_NAME, "page-heading")  # зарегистрированный профиль
    LOCATOR_SHOP_CONFIRM_LOGIN_PAGE = (By.CLASS_NAME, "navigation_page")  # Надпись на странице логина
    LOCATOR_SHOP_MAIN_PAGE_GOOD = (By.CLASS_NAME, "product-container")  # выбор товара
    LOCATOR_SHOP_LIKE_GOOD = (By.ID, "wishlist_button")  # добавление в избранное
    LOCATOR_SHOP_LOGIN_WISHLIST = (By.CLASS_NAME, "lnk_wishlist")  # страница wishlist
    LOCATOR_SHOP_LOGIN_WISHLIST_CONFIRM = (By.CSS_SELECTOR, "#block-history > table > thead > tr > th:nth-child(4)")
    # подверждение избранного товара


class CartPageLocators:
    """Locators for cart page"""
    CART_PAGE_TITLE = "Order-My Store"
    LOCATOR_SHOP_CART_LINK = (By.CSS_SELECTOR,
                              "#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a")  # локатор для перехода на страницу корзины
    LOCATOR_SHOP_CART_CONFIRM = (By.CSS_SELECTOR, "#center_column > p")  # надпись в корзине "Your shopping cart is
    # empty."
    LOCATOR_SHOP_CART_CHOICE = (By.CSS_SELECTOR, "#center_column > ul > li")  # локатор выбора товара (футболка)
    LOCATOR_SHOP_CART_ADD = (By.NAME, "Submit")  # локатор добавления в корзину
    LOCATOR_SHOP_CART_ALERT = (By.CSS_SELECTOR, "#layer_cart > div.clearfix > div.layer_cart_cart.col-xs-12.col-md-6 "
                                                "> div.button-container > a")
    LOCATOR_SHOP_CART_CONFIRM_ORDER = (By.CSS_SELECTOR, "#cart_title > span")  # подверждение наличия товара в корзине
