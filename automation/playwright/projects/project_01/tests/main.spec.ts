//? Imports
import { productsPage } from "../library/products";
import { loginPage } from "../library/login";
import { hamburgerMenu } from "../library/hamburger";
import { test } from '@playwright/test'


//? Variables
const wrongInput = 'test';
const correctUsername = 'standard_user';
const correctPassword = 'secret_sauce';


//? Tests
test('as the user i would try to log in', async ({page})=>{
    const login = new loginPage(page);

// --- Navigate to site ---
    await login.navigateToSite();

// --- Sad Flow Tests ---
    await login.noInput('','');
    await login.wrongInput(wrongInput,wrongInput);
    await login.noPassword(wrongInput);
    await login.noUsername(wrongInput);

// --- Happy Flow Test ---
    await login.login(correctUsername,correctPassword);
})


test('as the user i would navigate the products page', async ({page})=>{
    const products = new productsPage(page);
    const login = new loginPage(page);

// --- Login first ---
    await login.navigateToSite();
    await login.login(correctUsername,correctPassword);

// --- Navigate through products, view them, add them and then remove them from the basket through the product page ---
    await products.viewAddRemoveProduct('Sauce Labs Backpack');
    await products.viewAddRemoveProduct('Sauce Labs Bike Light');
    await products.viewAddRemoveProduct('Sauce Labs Bolt T-Shirt');
    await products.viewAddRemoveProduct('Sauce Labs Fleece Jacket');
    await products.viewAddRemoveProduct('Sauce Labs Onesie');
    await products.viewAddRemoveProduct('Test.allTheThings() T-Shirt (Red)');
})


test('as the user i would use the hamburger menu', async ({page})=>{
    const hamburger = new hamburgerMenu(page);
    const login = new loginPage(page);

// --- Login first ---
    await login.navigateToSite();
    await login.login(correctUsername,correctPassword);

// --- Use the hamburger menu ---
    await hamburger.aboutSidebar();
    await hamburger.logoutSidebar();
    await hamburger.allItemsSidebar();
})



