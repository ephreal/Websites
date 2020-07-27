window.addEventListener('load', function () {
    var mobile_label = document.getElementById("mobile-toggle-label");
    mobile_label.addEventListener("click", toggle_direction);
})

function toggle_direction() {
    var label = document.getElementById("mobile-toggle-label");
    if (label.classList[0]) {
        label.classList.remove("mobile-label-rotated");
        console.log("Class Removed");
    }
    else {
        console.log("Added class")
        label.classList.add("mobile-label-rotated");
    }
}
