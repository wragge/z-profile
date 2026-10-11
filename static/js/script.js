let filters = document.querySelectorAll(".filter");
for (filter of filters) {
    let filterValue = filter.dataset.filter;
    filter.addEventListener("click", function() {
        for (let item of document.querySelectorAll(`li.publication`)) {
            item.classList.remove("is-hidden");
        }
        if (this.classList.contains("is-light")) {
            this.classList.remove("is-light");
        } else {
            let selected = document.querySelector(".is-light")
            if (selected) {
                selected.classList.remove("is-light");
            }
            this.classList.add("is-light")
            for (let item of document.querySelectorAll(`li.publication:not(.${filterValue})`)) {
                item.classList.toggle("is-hidden");
            }
        }
        for (let heading of document.querySelectorAll("h2")) {
            let hidden = true;
            for (let listItem of heading.nextElementSibling.querySelectorAll("li")) {
                if (!listItem.classList.contains("is-hidden")) {
                    hidden = false;
                }
            }
            if (hidden === true) {
                heading.classList.add("is-hidden");
            } else {
                heading.classList.remove("is-hidden");
            }

        }
    });
}