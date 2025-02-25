module.exports = {
    // Use postcss-html to process Vue files correctly
    customSyntax: "postcss-html",
    overrides: [
      {
        files: ["*.vue"],
        customSyntax: "postcss-html",
      },
    ],
    rules: {},
  }
  