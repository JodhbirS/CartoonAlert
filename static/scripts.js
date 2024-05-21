document.addEventListener("DOMContentLoaded", function () {
    const phoneInputField = document.querySelector("#phone");
    const phoneInput = window.intlTelInput(phoneInputField, {
        initialCountry: "ca",
        onlyCountries: ["ca"]
    });

    const form = document.getElementById("phone-form");
    form.addEventListener("submit", function(event) {
        const phoneNumber = phoneInput.getNumber();
        phoneInputField.value = phoneNumber;
    });
});