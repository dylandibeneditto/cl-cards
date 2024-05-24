#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

class Flashcard {
 public:
  std::string front;
  std::string back;
};

void displayNav() {
  std::cout << "cl-cards | # of cards | `help`" << std::endl;
}

void clearScreen() {
#ifdef _WIN32
  system("cls");
#else
  system("clear");
#endif
  displayNav();
}

void displayHelp() {
  std::cout << "commands: written, exit, changeset, list" << std::endl;
}

bool confirmExit() {
  std::cout << "are you sure you want to exit? (y/n): " << std::endl;
  char exitChoice;
  std::cin >> exitChoice;
  return (exitChoice == 'y' || exitChoice == 'Y');
}

std::vector<std::string> getSetFiles() {
  std::vector<std::string> setFiles;
  std::filesystem::path exePath = std::filesystem::current_path();

  for (const auto& entry : std::filesystem::directory_iterator(exePath)) {
    if (entry.is_regular_file() && entry.path().extension() == ".set") {
      setFiles.push_back(entry.path().stem().string());
    }
  }
  return setFiles;
}

std::vector<Flashcard> readSet(std::vector<Flashcard>& flashcards,
                               const std::string& file) {
  std::ifstream infile(file);
  if (!infile) {
    std::cerr << "Unable to open file: " << file << std::endl;
    return flashcards;
  }

  std::cout << "Flashcards are now set to: " << file << std::endl;

  std::stringstream buffer;
  buffer << infile.rdbuf();
  std::string fileContent = buffer.str();
  infile.close();

  std::istringstream iss(fileContent);
  std::string token;
  while (std::getline(iss, token, ';')) {
    size_t colonPos = token.find(':');
    if (colonPos != std::string::npos) {
      Flashcard fc;
      fc.front = token.substr(0, colonPos);
      fc.back = token.substr(colonPos + 1);
      flashcards.push_back(fc);
    }
  }
  return flashcards;
}
std::vector<Flashcard> changeSet(std::vector<Flashcard> flashcards) {
  std::string file;
  std::cout << "Found sets in this directory" << std::endl;
  for (const auto& pf : getSetFiles()) {
    std::cout << "> " << pf << std::endl;
  }
  std::cin >> file;
  std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
  file += ".set";

  return readSet(flashcards, file);
}

int main() {
  std::vector<Flashcard> flashcards;
  bool exit = false;
  clearScreen();
  flashcards = changeSet(flashcards);

  while (!exit) {
    clearScreen();
    std::string cmd;
    std::cin >> cmd;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

    if (cmd == "help") {
      clearScreen();
      displayHelp();
    } else if (cmd == "exit") {
      if (confirmExit()) {
        exit = true;
      }
    } else if (cmd == "cs") {
      clearScreen();
      flashcards = changeSet(flashcards);

    } else if (cmd == "list") {
      for (const auto& card : flashcards) {
        std::cout << "Q: " << card.front << " | A: " << card.back << std::endl;
      }
    } else {
      std::cout << "Command unknown: " << cmd << std::endl;
    }

    if (!exit) {
      std::cout << "[ enter ]";
      std::cin.get();
    }
  }

  return 0;
}
