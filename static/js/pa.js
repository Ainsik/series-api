async function apiPost(url, year_from, year_to) {
	await fetch(url, {
		headers: {
			Accept: "application/json",
			"Content-Type": "application/json",
		},
		method: "POST",
		body: JSON.stringify({ year_from, year_to }),
	})
		.then((res) => res.json())
		.then((data) => {
			const ulist = document.querySelector("ul");
			ulist.innerHTML = "";
			data.actors.forEach((element) => {
				const li = document.createElement("li");
				ulist.appendChild(li);
				li.textContent = element.name;
			});
		});
}


const form = document.querySelector("#form");
form.addEventListener("submit", (event) => {
	event.preventDefault();
	apiPost("/pa", event.target[0].value, event.target[1].value);
});
