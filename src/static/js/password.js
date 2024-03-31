const passwordIcon = document.querySelector("#passwordIcon");
const passwordBox = document.querySelector("#password");


let passwordShowed = false;
function showPassword() {
    passwordShowed = true;
    passwordIcon.className = "fa-regular fa-eye-slash";
    passwordBox.type = "text";
}
function hidePassword() {
    passwordShowed = false;
    passwordIcon.className = "fa-regular fa-eye";
    passwordBox.type = "password";
}

passwordIcon.addEventListener("click", () => {
    passwordShowed ? hidePassword() : showPassword();
});