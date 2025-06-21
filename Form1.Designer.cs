namespace Dandilion
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            DownloadButton = new Button();
            textBox1 = new TextBox();
            comboBox1 = new ComboBox();
            richTextBox1 = new RichTextBox();
            ProgressBar = new ProgressBar();
            label1 = new Label();
            label2 = new Label();
            menuStrip1 = new MenuStrip();
            AboutStripMenuTool = new ToolStripMenuItem();
            menuStrip1.SuspendLayout();
            SuspendLayout();
            // 
            // DownloadButton
            // 
            resources.ApplyResources(DownloadButton, "DownloadButton");
            DownloadButton.Name = "DownloadButton";
            DownloadButton.UseVisualStyleBackColor = true;
            // 
            // textBox1
            // 
            resources.ApplyResources(textBox1, "textBox1");
            textBox1.BackColor = SystemColors.Window;
            textBox1.Name = "textBox1";
            // 
            // comboBox1
            // 
            resources.ApplyResources(comboBox1, "comboBox1");
            comboBox1.FormattingEnabled = true;
            comboBox1.Items.AddRange(new object[] { resources.GetString("comboBox1.Items"), resources.GetString("comboBox1.Items1"), resources.GetString("comboBox1.Items2"), resources.GetString("comboBox1.Items3") });
            comboBox1.Name = "comboBox1";
            // 
            // richTextBox1
            // 
            resources.ApplyResources(richTextBox1, "richTextBox1");
            richTextBox1.BackColor = SystemColors.Window;
            richTextBox1.DetectUrls = false;
            richTextBox1.Name = "richTextBox1";
            richTextBox1.ReadOnly = true;
            // 
            // ProgressBar
            // 
            resources.ApplyResources(ProgressBar, "ProgressBar");
            ProgressBar.Name = "ProgressBar";
            ProgressBar.Value = 5;
            // 
            // label1
            // 
            resources.ApplyResources(label1, "label1");
            label1.Name = "label1";
            // 
            // label2
            // 
            resources.ApplyResources(label2, "label2");
            label2.Name = "label2";
            // 
            // menuStrip1
            // 
            resources.ApplyResources(menuStrip1, "menuStrip1");
            menuStrip1.Items.AddRange(new ToolStripItem[] { AboutStripMenuTool });
            menuStrip1.Name = "menuStrip1";
            // 
            // AboutStripMenuTool
            // 
            resources.ApplyResources(AboutStripMenuTool, "AboutStripMenuTool");
            AboutStripMenuTool.Name = "AboutStripMenuTool";
            // 
            // Form1
            // 
            resources.ApplyResources(this, "$this");
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.Control;
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(ProgressBar);
            Controls.Add(richTextBox1);
            Controls.Add(comboBox1);
            Controls.Add(textBox1);
            Controls.Add(DownloadButton);
            Controls.Add(menuStrip1);
            MainMenuStrip = menuStrip1;
            MaximizeBox = false;
            MdiChildrenMinimizedAnchorBottom = false;
            Name = "Form1";
            menuStrip1.ResumeLayout(false);
            menuStrip1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button DownloadButton;
        private TextBox textBox1;
        private ComboBox comboBox1;
        private RichTextBox richTextBox1;
        private ProgressBar ProgressBar;
        private Label label1;
        private Label label2;
        private MenuStrip menuStrip1;
        private ToolStripMenuItem AboutStripMenuTool;
    }
}
