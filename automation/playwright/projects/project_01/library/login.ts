import {Page, expect} from '@playwright/test';
export class LoginPage {
    constructor(private page: Page) {}

    async NavigateToSite() {
        await this.page.goto('https://www.saucedemo.com/');
    }

    async NoInput(username: string, password: string) {
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Epic sadface: Username is required')).toBeVisible();
    }

    async WrongInput(username: string, password: string) {
        await this.page.fill('#user-name', username);
        await this.page.fill('[name="password"]', password)
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Epic sadface: Username and password do not match any user in this service')).toBeVisible();
    }

    async NoUsername(password: string) {
        await this.page.fill('#user-name', '');
        await this.page.fill('[name="password"]', password)
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Epic sadface: Username is required')).toBeVisible();
    }
    
    async NoPassword(username: string) {
        await this.page.fill('#user-name', username);
        await this.page.fill('[name="password"]', '')
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Epic sadface: Password is required')).toBeVisible();
    }

    async Login(username: string, password: string) {
        await this.page.fill('#user-name', username);
        await this.page.fill('[name="password"]', password)
        await this.page.click('#login-button');
        await expect(this.page.locator('text=Products')).toBeVisible()
    }
}
