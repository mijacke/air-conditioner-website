module.exports = {
    extends: ["stylelint-config-recommended-vue"],
    
    // Override how .vue files are parsed, so stylelint knows about <style> blocks
    overrides: [
      {
        files: ["**/*.vue"],
        customSyntax: "postcss-html"
      }
    ],
    rules: {}
  }
  