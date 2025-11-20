import {Page} from '@playwright/test';
export class productsPage {
    constructor(private page: Page) {}

async viewAddRemoveProduct(productName: string) {
    await this.page.click(`text=${productName}`);
    await this.page.click('text=Add to cart');
    await this.page.click('text=Remove');
    await this.page.goBack();
}

}