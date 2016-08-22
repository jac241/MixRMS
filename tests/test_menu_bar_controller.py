from unittest import TestCase
from mixrms.menubar import MenuBarController, FileValidator
from mixrms.plot import AnalysisController
from unittest.mock import Mock, create_autospec, patch


class TestMenuBarController(TestCase):

    def setUp(self):
        self.file_validator = create_autospec(FileValidator)
        self.analysis_controller = create_autospec(AnalysisController)
        self.uut = MenuBarController(
            file_validator=self.file_validator,
            analysis_controller=self.analysis_controller)

    @patch('mixrms.menubar.filedialog.askopenfilename')
    def test_load_file_should_invoke_analysis_controller_if_file_valid(self, mock_dialog):
        mock_dialog.return_value = 'test'
        self.file_validator.is_valid_wave_file.return_value = True
        self.analysis_controller.analyze_file.assert_called_once_with('test')
