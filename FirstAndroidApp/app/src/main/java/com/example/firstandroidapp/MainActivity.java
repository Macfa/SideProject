package com.example.firstandroidapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.Layout;
import android.widget.GridLayout;
import android.widget.TextView;

import org.w3c.dom.Text;

import static android.view.Gravity.CENTER;

public class MainActivity extends AppCompatActivity {

    private GridLayout Main_GL_Items;
    private TextView Header_TV_;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Main_GL_Items = findViewById(R.id.Main_GL_Items);

        //GridLayout MainMenuList = new GridLayout(this);
        Main_GL_Items.setOrientation(GridLayout.HORIZONTAL);
        Main_GL_Items.setRowCount(1);
        Main_GL_Items.setColumnCount(1);

        /*
        GridLayout.LayoutParams MainMenuListParams = new GridLayout.LayoutParams();
        MainMenuListParams.setGravity(CENTER);
        MainMenuListParams.height = GridLayout.LayoutParams.MATCH_PARENT;
        MainMenuListParams.width = GridLayout.LayoutParams.MATCH_PARENT;

    */


        TextView txt = new TextView(this);
        txt.setHeight(500);
        txt.setWidth(500);
        txt.setText("asdasdasd");



        //MainMenuList.setLayoutParams(MainMenuListParams);
        Main_GL_Items.addView(txt);

    }
}
