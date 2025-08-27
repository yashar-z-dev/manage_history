# 🧹 manage-history


## 🎯 Purpose

**manage-history** is built for developers who want more than just a clean terminal—they want insight, control, and speed.

This tool simplifies and enhances the way shell history is handled, backed up, and reused. It’s not just about deleting old commands—it's about unlocking the power hidden in your past workflows.

### 🔍 Core Goals

- **Automatic backups** of history files for safe archiving and future search.
- **Sorting and deduplication** with the `-s` flag to reduce noise and highlight meaningful commands.
- **Recovery of broken autocompletion**, restoring smooth shell behavior by reloading cleaned history files.
- **Simplified command usage**, replacing complex chains of shell commands with a single, efficient invocation.
- **Keyword and pattern filtering**, allowing precise control over what stays and what goes.

### 🌱 Future Vision

- **Autocomplete enhancement**, with tools to personalize and optimize shell suggestions based on actual usage.
- **Smart presets** for beginners, evolving into fully customizable setups for power users.
- **Command usage analytics**, identifying frequently used patterns and suggesting automation or aliases.
- **Community-curated history files**, sharing popular and effective command sets for common tasks.
- **Integration with external tools**, enabling automatic execution of high-impact commands and smarter autocompletion.

This project is for developers who care about clarity, performance, and making their terminal history work for them—not against them.

---

## 🚀 Installation

### 1. Clone the repository
```
git clone https://github.com/yashar-z-dev/manage_history.git
cd manage_history
```
### 2. Install with pip
```
pipx install .
```
### 3. Verify installation
```
manage-history -h
```
If no errors appear, the tool is ready to use. You can safely delete the project folder afterward.

---

## 🛠️ Usage
```
manage-history [OPTIONS]
```
### Options:

| Option | Description |
|--------|-------------|
| -k, --keyword | Remove lines containing a specific keyword |
| -l, --lines | Remove a range of lines (e.g., 12-15) |
| -r, --regex | Remove lines matching a regex pattern |
| -e, --exclude | Exclude lines containing this string |
| --backup-dir | Directory to save backup files (default: ~/all-history) |
| -s, --sort | Sort and clean the input file |
| -i, --input | Specify a custom input file |
| --debug | Enable debug mode for verbose output |

🔒 Backups are automatically created in ~/all-history unless a custom path is provided.

---

## 📦 Examples

- Remove all lines containing `rm`:
```
  manage-history -k rm
```
- Remove lines 20 through 30:
```
  manage-history -l 20-30
```
- Remove dangerous commands using regex:
```
  manage-history -r 'sudo\s+rm\s+-rf'
```
- Sort and clean `.bash_history`:
```
  manage-history -s -i ~/.bash_history
```
- Remove sensitive entries and save backup to a custom directory:
```
  manage-history -k password --backup-dir ~/history_backups
```
---

## 🤝 Contributing

I'm looking for motivated developers who are passionate about building effective tools.

Whether you're interested in improving performance, adding new features, or expanding compatibility with other shells (like fish or PowerShell), your contributions are welcome.

You can:
- Submit pull requests
- Open issues for bugs or feature suggestions
- Join discussions to share ideas

---

## 📄 License

This project is licensed under the MIT License.
