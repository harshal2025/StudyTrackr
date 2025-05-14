window.onload = function () {
    console.log("StudyTrackr loaded 🚀");

    if (window.location.pathname === "/subjects") {
        const btn = document.getElementById("helloBtn");
        if (btn) {
            btn.addEventListener("click", function () {
                alert("Keep grinding, legend! 📚💪");
            });
        }
    }
};
