function handoverto(element, gotolink) {
    document.getElementById(element).onclick = (e) => {
        window.location.href = gotolink
    }
}

handoverto("gfeed", "/feedback")
handoverto("generate", "/generate")


const generatebtn = document.getElementById("generate")
generatebtn.addEventListener("click", (e) => {
    const homepage = document.getElementById("homepageing")
    homepage.classList.toggle("visually-hidden")
    const generatepage = document.getElementById("generating")
    generatepage.classList.toggle("visually-hidden")
})
