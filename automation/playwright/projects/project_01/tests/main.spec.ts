import { products_page } from "../library/products";
import { login_page } from "../library/login";
import { hamburger_menu } from "../library/hamburger";
import { test } from '@playwright/test'

test('as the user i would try to log in', async ({page})=>{
    const login = new login_page(page);
    await login.as_the_user_i_would_first_navigate_to_the_site();
    await login.as_the_user_i_would_forget_any_input('','');
    await login.as_the_user_i_would_input_the_wrong_data('test','test');
    await login.as_the_user_i_would_forget_my_password('test');
    await login.as_the_user_i_would_forget_my_username('test');
    await login.as_the_user_i_would_log_in_succesfully('standard_user','secret_sauce');
})

test('as the user i would navigate the products page', async ({page})=>{
    const products = new products_page(page);
    await products.as_the_user_i_would_navigate_to_page_and_log_in();
    await products.as_the_user_i_would_view_add_remove_the_product_backpack();
    await products.as_the_user_i_would_view_add_remove_the_product_TestAllTheThingsTShirt();
    await products.as_the_user_i_would_view_add_remove_the_product_bikeLight();
    await products.as_the_user_i_would_view_add_remove_the_product_boltTShirt();
    await products.as_the_user_i_would_view_add_remove_the_product_fleeceJacket();
    await products.as_the_user_i_would_view_add_remove_the_product_onesie();
})

test('as the user i would use the hamburger menu', async ({page})=>{
    const hamburger = new hamburger_menu(page);
    const products = new products_page(page);
    await products.as_the_user_i_would_navigate_to_page_and_log_in();
    await hamburger.as_the_user_i_would_press_the_about_button();
    await hamburger.as_the_user_i_would_press_the_logout_button();
    await hamburger.as_the_user_i_would_press_the_allitems_button();
})



