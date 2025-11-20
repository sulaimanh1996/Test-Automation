import {Page} from '@playwright/test'
import { LoginPage } from "../library/login";
export class HamrburgerMenu {
    constructor(private page:Page) {}

    async AboutButton() {
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#about_sidebar_link');
        await this.page.goBack();    
    }

    async LogoutButton() {
        const loginPage = new LoginPage(this.page);
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#logout_sidebar_link');
        await loginPage.Login('standard_user','secret_sauce');
    }

    async AllitemsButton() {
        await this.page.click('text=Sauce Labs Backpack');
        await this.page.click('#react-burger-menu-btn');
        await this.page.click('#inventory_sidebar_link');
    }
    
}