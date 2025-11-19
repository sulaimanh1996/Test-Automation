import { test } from '@playwright/test';
import { ProductsPage } from '../library/products';
import { LoginPage } from '../library/login';

test('Log In', async ({page})=>{

    const loginPage = new LoginPage(page);
    //navigate to page
    await loginPage.NavigateToPage();
    //sad-flow no input
    await loginPage.LogInSadFlowNoInput('', '');
    //sad-flow wrong input
    await loginPage.LogInSadFlowWrongInput('test', 'test');
    //sad-flow no username
    await loginPage.LogInSadFlowNoUsername('test');
    //sad-flow no password
    await loginPage.LogInSadFlowNoPassword('test');
    //happy-flow login
    await loginPage.LogInHappyFlow('standard_user', 'secret_sauce')

})

test('Product Page', async ({page})=>{

    const productsPage = new ProductsPage(page);  
    //navigate to page and login
    await productsPage.NavigateToPageAndLogin();
    //view/Add/Remove product Sauce Labs Backpack
    await productsPage.ViewAddRemoveBackpack();
    //view/Add/Remove product Sauce Labs Bike Light
    await productsPage.ViewAddRemoveBikeLight();
    //view/Add/Remove product Sauce Labs Bolt T-Shirt
    await productsPage.ViewAddRemoveBoltTShirt();
    //view/Add/Remove product Sauce Labs Fleece Jacket
    await productsPage.ViewAddRemoveFleeceJacket();
    //view/Add/Remove product Sauce Labs Onesie
    await productsPage.ViewAddRemoveOnesie();
    //view/Add/Remove product Test.allTheThings() T-Shirt (Red)
    await productsPage.ViewAddRemoveTestAllTheThingsTShirt();
})