const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    const database = process.argv[2];
    try {
      const students = await readDatabase(database);
      let response = 'This is the list of our students\n';

      Object.keys(students).sort((a, b) => a.localeCompare(b)).forEach((field) => {
        const studentList = students[field];
        response += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}\n`;
      });

      res.status(200).send(response.trim());
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const database = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const students = await readDatabase(database);
      const studentList = students[major] || [];

      res.status(200).send(`List: ${studentList.join(', ')}`);
    } catch (error) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
