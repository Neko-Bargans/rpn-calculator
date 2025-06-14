from unittest.mock import patch
import app.services.stack as stack_services


class TestListOeprands:
    def test_return_successfully(self):
        assert stack_services.list_operands() == ["+", "-", "*", "/"]


class TestCreateStack:
    @patch("app.services.stack.session")
    def test_create_successfully(self, mock_session):
        new_stack = stack_services.create_stack()

        assert (
            new_stack.stack  # pylint: disable=use-implicit-booleaness-not-comparison
            == []
        )
        mock_session.add.assert_called_once_with(new_stack)
        mock_session.commit.assert_called_once()


class TestListStacks:
    @patch("app.services.stack.session")
    def test_list_successfully(self, mock_session, mock_stack):
        mock_session.query.return_value.all.return_value = [mock_stack]
        stacks = stack_services.list_stacks()
        assert len(stacks) == 1
        assert stacks[0] == mock_stack


class TestGetStackById:
    def test_get_fails_with_invalid_id(self):
        pass

    def test_get_fails_with_not_found(self):
        pass

    def test_get_successfully(self):
        pass


class TestDeleteStackByid:
    def test_delete_fails_with_invalid_id(self):
        pass

    def test_delete_fails_with_not_found(self):
        pass

    def test_delete_successfully(self):
        pass


class TestAddValueToStackById:
    def test_add_fails_with_invalid_id(self):
        pass

    def test_add_fails_with_invalid_value(self):
        pass

    def test_add_fails_with_not_found(self):
        pass

    def test_add_successfully(self):
        pass


class TestApplyOperandOnAStackById:
    def test_apply_fails_with_invalid_id(self):
        pass

    def test_apply_fails_with_invalid_operand(self):
        pass

    def test_apply_fails_with_not_found(self):
        pass

    def test_apply_fails_with_unknown_operand(self):
        pass

    def test_apply_fails_with_cannot_divide_by_0(self):
        pass

    def test_apply_fails_with_insuffient_values(self):
        pass

    def test_apply_successfully(self):
        pass
