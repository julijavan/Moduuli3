const form = document.getElementById('tv-search-form');
const resultsDiv = document.getElementById('results');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const query = document.getElementById('query').value.trim();
  if (!query) return;

  const url = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;

  try {
    const response = await fetch(url);
    const data = await response.json();

    console.log(data);

    resultsDiv.innerHTML = '';

    data.forEach(tvShow => {
      const show = tvShow.show;

      const article = document.createElement('article');

      const title = document.createElement('h2');
      title.textContent = show.name;

      const link = document.createElement('a');
      link.href = show.url;
      link.textContent = 'More details';
      link.target = '_blank';

      const image = document.createElement('img');
      if (show.image?.medium) {
        image.src = show.image.medium;
        image.alt = show.name;
      }

      const summary = document.createElement('div');
      summary.innerHTML = show.summary || 'No summary available.';

      article.appendChild(title);
      article.appendChild(link);
      if (show.image?.medium) article.appendChild(image);
      article.appendChild(summary);

      resultsDiv.appendChild(article);
    });
  } catch (error) {
    console.error('Error fetching data:', error);
    resultsDiv.innerHTML = '<p>Oho! Jokin meni vikaan. :( yritä myöhemmin uudelleen.</p>';
  }
});