import {Page} from '@playwright/test';
export class products_page {
    constructor(private page: Page) {}

    async as_the_user_i_would_navigate_to_page_and_log_in() {
        await this.page.goto('https://www.saucedemo.com/');
        await this.page.fill('#user-name', 'standard_user');
        await this.page.fill('[name="password"]', 'secret_sauce')
        await this.page.click('#login-button');
    }

    async as_the_user_i_would_view_add_remove_the_product_backpack() {
        await this.page.click('text=Sauce Labs Backpack');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack();
    }

    async as_the_user_i_would_view_add_remove_the_product_bikeLight() {
        await this.page.click('text=Sauce Labs Bike Light');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack(); 
    }   

    async as_the_user_i_would_view_add_remove_the_product_boltTShirt() {
        await this.page.click('text=Sauce Labs Bolt T-Shirt');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack();
    } 

    async as_the_user_i_would_view_add_remove_the_product_fleeceJacket() {
        await this.page.click('text=Sauce Labs Fleece Jacket');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack(); 
    }   

    async as_the_user_i_would_view_add_remove_the_product_onesie() {
        await this.page.click('text=Sauce Labs Onesie');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack(); 
    }   

    async as_the_user_i_would_view_add_remove_the_product_TestAllTheThingsTShirt() {
        await this.page.click('text=Test.allTheThings() T-Shirt (Red)');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack(); 
    }   
}