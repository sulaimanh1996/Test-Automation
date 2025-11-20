import {Page, expect} from '@playwright/test';
export class login_page {
    constructor(private page: Page) {}

    async as_the_user_i_would_first_navigate_to_the_site() {
        await this.page.goto('https://www.saucedemo.com/');
    }

    async as_the_user_i_would_forget_any_input(username: string, password: string) {
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Epic sadface: Username is required')).toBeVisible();
    }

    async as_the_user_i_would_input_the_wrong_data(username: string, password: string) {
        await this.page.fill('#user-name', username);
        await this.page.fill('[name="password"]', password)
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Epic sadface: Username and password do not match any user in this service')).toBeVisible();
    }

    async as_the_user_i_would_forget_my_username(password: string) {
        await this.page.fill('#user-name', '');
        await this.page.fill('[name="password"]', password)
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Epic sadface: Username is required')).toBeVisible();
    }
    
    async as_the_user_i_would_forget_my_password(username: string) {
        await this.page.fill('#user-name', username);
        await this.page.fill('[name="password"]', '')
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Epic sadface: Password is required')).toBeVisible();
    }

    async as_the_user_i_would_log_in_succesfully(username: string, password: string) {
        await this.page.fill('#user-name', username);
        await this.page.fill('[name="password"]', password)
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Products')).toBeVisible()
    }
}
