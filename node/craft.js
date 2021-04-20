const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {

  const browser = await puppeteer.launch();

  const page = await browser.newPage();

  await page.goto('https://absolutasaude.com.br/landingpage.php');
  
  const resultOfCraft = await page.evaluate(()=>{

    const nodelist = document.querySelectorAll('.second-section img')

    const imgArray = [...nodelist]

    const result = imgArray.map( ({ src }) => ({ src }) )

    return result

  })

  fs.writeFile('dados.json', JSON.stringify(resultOfCraft, null, 2) , err => {
    if(err) throw new Error("this site have a captcha or other wrong.")

    console.log("Yes, nice craft 🤖")
  })
  
  await browser.close();
})();