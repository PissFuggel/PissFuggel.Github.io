class Bil {

    constructor(brand, color, bid){
        this.brand = brand
        this.color = color
        this.bid = bid
    }
}

let billista = []

async function getDataFromLocalStorage(){
    try{
        billista =await JSON.parse(localStorage.getItem("bilarlistan"))

        //Om billistan är tom Null från local storage
        if (billista == null){
            billista = []
        }

        lista_bilar_div.innerHTML=""

        billista.forEach(createHtmlBillista)

    }
    catch (e){
        console.log(`Fel: ${e}`)
    }
}

getDataFromLocalStorage()


function addButtonClick(){
    //console.log(Fabrikat: ${brand.value} Färg: ${color.value})
    const now = Date.now()
    const id = now.toString()
    let brandname = brand.value

    if (brandname != ""){
        //Lägg till bil
        let car = new Bil(brand.value, color.value, id)
        billista.push(car)

        localStorage.setItem("bilarlistan", JSON.stringify(billista))
        brand.value=""
        color.value=""

        lista_bilar_div.innerHTML= "";

        billista.forEach(createHtmlBillista)
    }
    else
        alert("Måste fylla i fabrikat")

    brand.focus()
}
//-------------------------------------------
// createHtmlBillista() som arrowfunction

const createHtmlBillista = (bil) => {
    //skapar element
    const bildiv = document.createElement('div')
    bildiv.className = "bil_div_element"

    const bilH2 = document.createElement('H3')
    const bilPcolor = document.createElement('P')
    const bilDelButton = document.createElement('button')

    bilH2.innerText = `Brand: ${bil.brand}`
    bilPcolor.innerText = `Färg: ${bil.color}`
    bilDelButton.innerText = "Delete"
    bilDelButton.id = bil.bid

    bildiv.append(bilH2, bilPcolor, bilDelButton)
    lista_bilar_div.appendChild(bildiv)
}


const addbutton = document.getElementById("addbutton")
addbutton.addEventListener("click", addButtonClick)
const brand = document.getElementById("brand")
const color = document.getElementById("color")
const lista_bilar_div = document.getElementById("listabilarDiv")

//deleteBil--------------------
let deleteBil = (e) => {
    const ny_billista = billista.filter((o, i) => o.bid != e.target.id)

    billista = ny_billista
    //skriver till locla storage
    localStorage.setItem("bilarlistan", JSON.stringify(billista))
    //läser från localstorage och visar sen på den nya listan
    getDataFromLocalStorage();

}

window.addEventListener("click", deleteBil);