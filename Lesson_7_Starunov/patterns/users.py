


class StudentMapper:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.table_name = 'student'

    def all(self):
        self.cursor.execute(f"""
            SELECT * FROM {self.table_name};
        """)
        result = []
        for id_, firstname, lastname, age in self.cursor.fetchall():
            student = Student(firstname, lastname, age)
            student.id = id_
            result.append(student)
        return result

    def find_by_id(self, id_):
        self.cursor.execute(f"""
            SELECT id, firstname, lastname, age FROM {self.table_name} WHERE id=?;
        """, (id_,))
        result = self.cursor.fetchone()
        if result:
            return Student(*result)
        else:
            raise RecordNotFoundException(f'record with id={id} not found')

    def insert(self, obj):
        self.cursor.execute(f"""
            INSERT INTO {self.table_name} (firstname, lastname, age) VALUES (?, ?, ?);
        """, (obj.firstname, obj.lastname, obj.age))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, obj):
        self.cursor.execute(f"""
            UPDATE {self.table_name} SET firstname=? lastname=? age=? WHERE id=?;
        """, (obj.firstname, obj.lastname, obj.age, obj.id))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, obj):
        statement = f""
        self.cursor.execute(f"""
            DELETE FROM {self.table_name} WHERE id=?
        """, (obj.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)
