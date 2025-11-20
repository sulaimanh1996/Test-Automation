import {Page} from '@playwright/test'
import { login_page } from "../library/login";
export class hamburger_menu {
    constructor(private page:Page) {}

    async as_the_user_i_would_press_the_about_button() {
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#about_sidebar_link');
        await this.page.goBack();    
    }

    async as_the_user_i_would_press_the_logout_button() {
        const loginPage = new login_page(this.page);
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#logout_sidebar_link');
        await loginPage.as_the_user_i_would_log_in_succesfully('standard_user','secret_sauce');
    }

    async as_the_user_i_would_press_the_allitems_button() {
        await this.page.click('text=Sauce Labs Backpack');
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#inventory_sidebar_link');
    }
    
}