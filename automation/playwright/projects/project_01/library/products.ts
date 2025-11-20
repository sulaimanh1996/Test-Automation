import {Page} from '@playwright/test';
export class ProductsPage {
    constructor(private page: Page) {}

    async ViewAddRemoveBackpack() {
        await this.page.click('text=Sauce Labs Backpack');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack();
    }

    async ViewAddRemoveBikeLight() {
        await this.page.click('text=Sauce Labs Bike Light');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack(); 
    }   

    async ViewAddRemoveBoltTShirt() {
        await this.page.click('text=Sauce Labs Bolt T-Shirt');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack();
    } 

    async ViewAddRemoveFleeceJacket() {
        await this.page.click('text=Sauce Labs Fleece Jacket');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack(); 
    }   

    async ViewAddRemoveOnesie() {
        await this.page.click('text=Sauce Labs Onesie');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack(); 
    }   

    async ViewAddRemoveTestAllTheThingsTShirt() {
        await this.page.click('text=Test.allTheThings() T-Shirt (Red)');
        await this.page.click('text=Add to cart');
        await this.page.click('text=Remove');
        await this.page.goBack(); 
    }   

}