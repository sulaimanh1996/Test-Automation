import { ProductsPage } from "../library/products";
import { LoginPage } from "../library/login";
import { HamrburgerMenu } from "../library/hamburger";
import { test } from '@playwright/test'

const WrongInput = 'test';
const CorrectUsername = 'standard_user';
const CorrectPassword = 'secret_sauce';

test('as the user i would try to log in', async ({page})=>{
    const login = new LoginPage(page);
    await login.NavigateToSite();
    await login.NoInput('','');
    await login.WrongInput(WrongInput,WrongInput);
    await login.NoPassword(WrongInput);
    await login.NoUsername(WrongInput);
    await login.Login(CorrectUsername,CorrectPassword);
})

test('as the user i would navigate the products page', async ({page})=>{
    const products = new ProductsPage(page);
    const login = new LoginPage(page);
    await login.NavigateToSite();
    await login.Login(CorrectUsername,CorrectPassword);
    await products.ViewAddRemoveBackpack();
    await products.ViewAddRemoveBikeLight();
    await products.ViewAddRemoveBoltTShirt();
    await products.ViewAddRemoveFleeceJacket();
    await products.ViewAddRemoveOnesie();
    await products.ViewAddRemoveTestAllTheThingsTShirt();
})

test('as the user i would use the hamburger menu', async ({page})=>{
    const hamburger = new HamrburgerMenu(page);
    const products = new ProductsPage(page);
    const login = new LoginPage(page);
    await login.NavigateToSite();
    await login.Login(CorrectUsername,CorrectPassword);
    await hamburger.AboutButton();
    await hamburger.LogoutButton();
    await hamburger.AllitemsButton();
})



