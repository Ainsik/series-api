const all_actors_btn = document.querySelectorAll(".name");

all_actors_btn.forEach((actor_btn) => {
	actor_btn.addEventListener("click", (e) => {
		const div = e.target.querySelector(".hiden");
		// div.toggleAttribute("hidden");
		const result = div.hasAttribute("hidden");
		result
			? div.removeAttribute("hidden")
			: div.setAttribute("hidden", "hidden");
	});
});
