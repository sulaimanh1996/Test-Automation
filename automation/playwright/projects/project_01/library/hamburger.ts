//? Imports and Exports
import {Page} from '@playwright/test'
import { loginPage } from "../library/login";
export class hamburgerMenu {
    constructor(private page:Page) {}

//? Selectors
    private aboutLink = '#about_sidebar_link';
    private logoutLink = '#logout_sidebar_link'
    private allitemsLink = '#inventory_sidebar_link'
    private hamburgerButton = '#react-burger-menu-btn'
    private closeMenuButton = '#react-burger-cross-btn'
    private username = 'standard_user'
    private password = 'secret_sauce'

//? Methods
    async aboutSidebar() {
        await this.page.click(this.hamburgerButton);
        await this.page.click(this.aboutLink);
        await this.page.goBack();    
    }

    async logoutSidebar() {
        const login = new loginPage(this.page);
        await this.page.click(this.hamburgerButton);
        await this.page.click(this.logoutLink);
        await login.login(this.username,this.password);
    }

    async allItemsSidebar() {
        await this.page.click('text=Sauce Labs Backpack');
        await this.page.click(this.hamburgerButton);
        await this.page.click(this.allitemsLink);
    }
    
}