const form =
    document.querySelector("#prediction-form");

const sizeInput =
    document.querySelector("#size");

const bedroomsInput =
    document.querySelector("#bedrooms");

const bathroomsInput =
    document.querySelector("#bathrooms");

const button =
    document.querySelector("#predict-button");

const errorMessage =
    document.querySelector("#error-message");


// ==========================================
// FORM VALIDATION
// ==========================================

form.addEventListener(
    "submit",
    function (event) {

        errorMessage.innerText = "";

        errorMessage.style.display =
            "none";


        const size =
            Number(sizeInput.value);

        const bedrooms =
            Number(bedroomsInput.value);

        const bathrooms =
            Number(bathroomsInput.value);


        // House size

        if (
            !Number.isFinite(size) ||
            size < 300
        ) {

            event.preventDefault();

            errorMessage.innerText =
                "House size should be at least 300 sq ft.";

            errorMessage.style.display =
                "block";

            return;
        }


        // Bedrooms

        if (
            !Number.isFinite(bedrooms) ||
            bedrooms < 1
        ) {

            event.preventDefault();

            errorMessage.innerText =
                "Bedrooms should be at least 1.";

            errorMessage.style.display =
                "block";

            return;
        }


        // Bathrooms

        if (
            !Number.isFinite(bathrooms) ||
            bathrooms < 1
        ) {

            event.preventDefault();

            errorMessage.innerText =
                "Bathrooms should be at least 1.";

            errorMessage.style.display =
                "block";

            return;
        }


        // Loading state

        button.innerText =
            "Predicting...";

        button.disabled = true;

    }
);


// ==========================================
// PRICE FORMATTING
// ==========================================

const priceElement =
    document.querySelector("#price");


if (priceElement) {

    const price =
        Number(
            priceElement.innerText
                .replace("₹", "")
                .replace(/,/g, "")
                .trim()
        );


    if (Number.isFinite(price)) {

        priceElement.innerText =
            "₹ " +
            Math.round(price)
                .toLocaleString("en-IN");

    }

}
