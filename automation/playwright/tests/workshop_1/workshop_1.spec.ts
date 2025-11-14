import {test, expect} from '@playwright/test';

test('Log In', async ({page})=>{
    await page.goto('https://www.saucedemo.com/');

    await page.click('#login-button');
    await expect(page.locator('text=Epic sadface: Username is required')).toBeVisible();

    await page.fill('#user-name', 'test');
    await page.fill('[name="password"]', 'test')
    await page.click('#login-button');
    await expect(page.locator('text=Epic sadface: Username and password do not match any user in this service')).toBeVisible();


    await page.fill('#user-name', '');
    await page.fill('[name="password"]', 'test')
    await page.click('#login-button');
    await expect(page.locator('text=Epic sadface: Username is required')).toBeVisible();

    await page.fill('#user-name', 'test');
    await page.fill('[name="password"]', '')
    await page.click('#login-button');
    await expect(page.locator('text=Epic sadface: Password is required')).toBeVisible();

    await page.fill('#user-name', 'standard_user');
    await page.fill('[name="password"]', 'secret_sauce')
    await page.click('#login-button');
    await expect(page.locator('text=Products')).toBeVisible()
})

test('Log In', async ({page})=>{
})
