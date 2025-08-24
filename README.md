# 🧹 manage-history

A reliable CLI tool for cleaning and managing shell history files with customizable filters, automatic backups, and user confirmation before deletion. Ideal for developers who care about security, clarity, and control in their terminal environment.

---

## 🚀 Installation

### 1. Clone the repository

git clone https://github.com/yashar-z-dev/manage_history.git
cd manage_history

### 2. Install with pip

pip install .

### 3. Verify installation

manage-history -h

If no errors appear, the tool is ready to use. You can safely delete the project folder afterward.

---

## 🛠️ Usage

manage-history [OPTIONS]

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
  manage-history -k rm

- Remove lines 20 through 30:
  manage-history -l 20-30

- Remove dangerous commands using regex:
  manage-history -r 'sudo\s+rm\s+-rf'

- Sort and clean `.bash_history`:
  manage-history -s -i ~/.bash_history

- Remove sensitive entries and save backup to a custom directory:
  manage-history -k password --backup-dir ~/history_backups

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
