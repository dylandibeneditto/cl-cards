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

void studyFlashcards(const std::vector<Flashcard>& flashcards) {
  if (flashcards.empty()) {
    std::cout << "No flashcards available. Please add some flashcards first."
              << std::endl;
    return;
  }
  // Implementation of studying flashcards
}

std::vector<std::string> getSetFiles() {
  std::vector<std::string> setFiles;
  std::filesystem::path exePath =
      std::filesystem::current_path();  // Get the directory of the executable

  // Iterate through the directory entries
  for (const auto& entry : std::filesystem::directory_iterator(exePath)) {
    if (entry.is_regular_file() && entry.path().extension() == ".set") {
      setFiles.push_back(
          entry.path().stem().string());  // Get filename without extension
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
  } else {
    std::cout << "flashcards are now set to: " << file << std::endl;
  }

  // Read the whole file into a string
  std::stringstream buffer;
  buffer << infile.rdbuf();
  std::string fileContent = buffer.str();
  infile.close();

  // Parse the string to extract flashcards
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

int main() {
  std::vector<Flashcard> flashcards;
  bool exit = false;

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
      std::string file;
      std::cout << "found sets in this directory" << std::endl;
      for (const auto& pf : getSetFiles()) {
        std::cout << "> " << pf << std::endl;
      }
      std::cin >> file;
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      file += ".set";  // Append the ".set" extension

      flashcards = readSet(flashcards, file);

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
