import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'Evaluation-new',
  templateUrl: './Evaluation-new.component.html',
  styleUrls: ['./Evaluation-new.component.scss']
})
export class EvaluationNewComponent {
  @ViewChild("EvaluationForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}