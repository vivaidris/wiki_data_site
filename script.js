document.getElementById("img_a").addEventListener("mouseover", MouseOverA);
document.getElementById("img_a").addEventListener("mouseout", MouseOut);

document.getElementById("img_b").addEventListener("mouseover", MouseOverB);
document.getElementById("img_b").addEventListener("mouseout", MouseOut);

document.getElementById("img_c").addEventListener("mouseover", MouseOverC);
document.getElementById("img_c").addEventListener("mouseout", MouseOut)

function removeTooltipImmediately() {
    const existing = document.getElementById("temp_id");
    if (existing) {
        // Remove the element immediately without waiting for fade out
        existing.remove();
    }
}

function MouseOverA() {
    removeTooltipImmediately();

    if (!document.getElementById("temp_id")) {
        const para = document.createElement("p");
        para.style.opacity = "0";
        para.style.transition = "opacity 0.3s ease";
        const node = document.createTextNode("This image shows a bar chart of how many paragraphs there is per article");
        para.appendChild(node);
        para.setAttribute("id", "temp_id");

        const element = document.getElementById("img_a_holder");
        element.appendChild(para);

        para.style.display = "block";
        para.style.position = "absolute";
        para.style.fontFamily = "Verdana, Geneva, Tahoma, sans-serif";

        requestAnimationFrame(() => {
            para.style.opacity = "1";
        });
    }
}

function MouseOverB() {
    removeTooltipImmediately();

    if (!document.getElementById("temp_id")) {
        const para = document.createElement("p");
        para.style.opacity = "0";
        para.style.transition = "opacity 0.3s ease";
        const node = document.createTextNode("This image shows a scatter chart of the average amount of words per paragraph");
        para.appendChild(node);
        para.setAttribute("id", "temp_id");

        const element = document.getElementById("img_b_holder");
        element.appendChild(para);

        para.style.display = "block";
        para.style.position = "absolute";
        para.style.fontFamily = "Verdana, Geneva, Tahoma, sans-serif";

        requestAnimationFrame(() => {
            para.style.opacity = "1";
        });
    }
}

function MouseOverC() {
    removeTooltipImmediately();

    if(!document.getElementById("temp_id")){
        const para = document.createElement("p");
        para.style.opacity = "0";
        para.style.transition = "opacity 0.3s ease";
        const node = document.createTextNode("This image shows a pie chart of how many articles have specific themes");
        para.appendChild(node);
        para.setAttribute("id", "temp_id");

        const element = document.getElementById("img_c_holder");
        element.appendChild(para);

        para.style.display = "block";
        para.style.position = "relative";
        para.style.positon = "right: 20px";
        para.style.alignContent = "center";
        para.style.fontFamily = "Verdana, Geneva, Tahoma, sans-serif";

        requestAnimationFrame(() => {
            para.style.opacity = "1"
        })
    }
}

function MouseOut() {
    const elmnt = document.getElementById("temp_id");
    if (elmnt) {
        elmnt.style.opacity = "0";  // start fade-out

        // Listen for the end of the opacity transition, then remove the element
        elmnt.addEventListener("transitionend", function handler() {
            elmnt.remove();
            elmnt.removeEventListener("transitionend", handler);  // clean up listener
        });
    }
}
