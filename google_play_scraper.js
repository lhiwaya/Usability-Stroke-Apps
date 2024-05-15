import("google-play-scraper")
  .then((module) => {
    const gplay = module.default;
    gplay
      .search({
        term: "stroke",
        num: 250,
        price: "free",
        country: "se",
        lang: "sw",
        fulldetail: "true",
      })
      .then((result) => {
        const fs = require("fs");
        const jsonData = JSON.stringify(result, null, 2);
        fs.writeFileSync("search_result.json", jsonData);
        console.log("Search result has been written to search_result.json");
      })
      .catch((error) => {
        console.error("Error searching:", error);
      });
  })
  .catch((error) => {
    console.error("Error loading google-play-scraper:", error);
  });
