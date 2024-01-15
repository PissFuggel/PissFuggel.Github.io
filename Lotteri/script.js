const antal_vinster = document.getElementById("antalvister")
const svaretdiv = document.getElementById("svar_div")

const vinster = ["En Panigale V4 2023", "Nitlott", "Direktimporterad ryss", "Härodlad canabis", "Nitlott", "En begagnad toaborste", "En begnagd morot", "En telefon från Huang Huang", "Avbetalning av Huang Huangs skulder", "Nisses gamla frisyr", "Nitlott", "Smuls glasögon med valfri dipp"]


function buttonClick(e){
    

    let vinst = `<h2>Dina lotter</h2>`;

    let  antalv = parseInt(antal_vinster.value);

    if (antalv < 4 && antalv > 0){

        for (i=0; i<antalv; i++){
            let slumptal = Math.floor(Math.random() * vinster.length);
            let t_vinst = vinster[slumptal];

            vinst += `<p> ${t_vinst} </p>`

        }

        svaretdiv.innerHTML = vinst;
    }
    else{

        alert("Du har valt för få eller för många lotter!")
    }

}