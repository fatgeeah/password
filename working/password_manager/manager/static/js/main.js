//display on click
const modalWrapper = document.querySelector(".modals-wrapper");
if (modalWrapper) {
    function displayModal(id) {
        const modal = document.getElementById(id);
        modalWrapper.style.display = "flex";
        modal.style.display = "flex";
        a.style.display ="none"

        //close
        const close = document.getElementById("close-modal");
        close.addEventListener("click", () => {
            modalWrapper.style.display = "none";
            modal.style.display = "none";   
            a.style.display ="none"
        } )
    }
}

const copies = document.querySelectorAll(".copy");
copies.forEach(copy => {
    copy.onclick = () => {
        let elementToCopy = copy.previousElementSibling;
        elementToCopy.select();
        document.execCommand("copy");
    }
})
