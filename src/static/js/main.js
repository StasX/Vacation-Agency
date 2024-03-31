

function validateCountry() {
    const countryBox = document.querySelector("#countryBox");
    const countryId = countryBox.value;
    return /^\d+$/.test(countryId);
}
function validateStartDate() {
    const startDateBox = document.querySelector("#startDate");
    const startDate = new Date(startDateBox.value);
    const dateNow = new Date();
    // I assume that user can start and end the vacation in current day
    const msg = (startDate < dateNow) ? "Start date should be in future." : "";
    startDateBox.setCustomValidity(msg);
    // Revalidate end date
    validateEndDate();
}
function validateEndDate() {
    const startDateBox = document.querySelector("#startDate");
    const startDate = new Date(startDateBox.value);
    const endDateBox = document.querySelector("#endDate");
    const endDate = new Date(endDateBox.value);
    const msg = (endDate < startDate) ? "End date can't be before start date." : "";
    endDateBox.setCustomValidity(msg);
}
// Add / Edit vacation form validation
function validateVacationForm(event) {
    event.preventDefault();
    const countryId = document.querySelector("#countryBox").value;
    if (validateCountry(countryId)) {
        validateForm(event);
    } else {
        // Show modal window
        showModal({
            title: '<i class="fa-solid fa-triangle-exclamation"></i>',
            text: "Please choice country"
        });
    }
}

// Validate any form
function validateForm(event) {
    if (event.target.checkValidity()) {
        event.target.submit();
    }
}

// Show image
function displayImage() {
    // Image to preview loaded file
    const preview = document.querySelector("#preview");
    // Get loaded file
    const file = document.querySelector('input[type="file"]').files[0];
    // Create FileReader
    const reader = new FileReader();
    // Preview loaded image
    reader.onload = () => {
        preview.src = reader.result;
    }
    // If file loaded and it image - preview it.
    if (file && /^image\/\w+$/.test(file.type)) {
        reader.readAsDataURL(file);
        // Change "Add button text"
        document.querySelector("#imgBtn").innerText="Change image";
    }
}

// Modal window creation
function showModal(props) {
    const cancelBtnText = props.cancelBtnText || "Cancel";
    const showCancelBtn = props.showCancelBtn;
    const cancelBtn = showCancelBtn ? `<button type="button" class="btn btn-dark" id="cancel">${cancelBtnText}</button>` : "";
    const okBtnText = props.okBtnText || "Ok";
    document.body.insertAdjacentHTML("afterend", `
    <div class="modal fade show" id="staticBackdropLive" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLiveLabel" style="display: block;" aria-modal="true" role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title" id="staticBackdropLabel">${props.title}</h1>
                </div>
                <div class="modal-body">
                    ${props.text}
                </div>
                <div class="modal-footer">
                    ${cancelBtn}
                    <button type="button" class="btn btn-dark" id="ok">${okBtnText}</button>
                </div>
            </div>
        </div>
    </div>`);
    // Add handlers for modal window
    const closeBtnId = showCancelBtn ? "cancel" : "ok";
    document.getElementById(closeBtnId).onclick = () => {
        // Remove modal window
        document.querySelector(".modal").remove();
        document.body.style.overflow = "auto";
    };
    if (showCancelBtn) {
        document.getElementById("ok").onclick = props.okBtnAction;
    }
    // Hide scrolling bar
    document.body.style.overflow = "hidden";
}

// Handle "delete" button click 
function deleteVacation(url) {
    // Show modal window
    showModal({
        title: '<i class="fa-solid fa-triangle-exclamation"></i>',
        text: "Are you really want to delete this vacation?",
        showCancelBtn: true,
        cancelBtnText: "No",
        okBtnText: "Yes",
        okBtnAction: () => {
            // Go to "vacation removing" url
            location.href = location.origin + url;
        }
    });
    // Add handlers for modal window
    document.getElementById("cancel").onclick = () => {
        // Remove modal window
        document.querySelector(".modal").remove();
        document.body.style.overflow = "auto";
    };
}

// Country selection
function selectCountry(name, id) {
    document.querySelector("#countryBox").value = id;
    document.querySelector("#countrySelector").innerText = name;
    // Set country validity
    validateCountry()
}



window.onload = () => {
    // Set two decimal places after the point
    const priceBox = document.getElementById("priceBox");
    if (priceBox) {
        if (priceBox.value) {
            priceBox.value = parseFloat(priceBox.value).toFixed(2);
        }
        priceBox.onblur = () => { if (priceBox.value) priceBox.value = parseFloat(priceBox.value).toFixed(2); }
    }

    // Run validations when form loaded"
    if (document.querySelector("#vacationForm")) {
        validateStartDate();
        validateEndDate();
    }
}