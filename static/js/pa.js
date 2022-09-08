async function apiGet(url) {
	let response = await fetch(url, {
		method: "GET",
	});
	if (response.ok) {
		return await response.json();
	}
}

async function apiPost(url, year_from, year_to) {
	let response = await fetch(url, {
		headers: {
			Accept: "application/json",
			"Content-Type": "application/json",
		},
		method: "POST",
		body: JSON.stringify(year_from, year_to),
	});
	if (response.ok) {
		return await response.json();
	}
}

async function paGet() {
	return await apiGet("/pa");
}
async function paPost() {
	return await apiPost("/pa", { year_from: year_from }, { year_to: year_to });
}

function init() {
	paGet();
	paPost();
}

init();
